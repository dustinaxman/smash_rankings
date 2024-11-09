import hashlib
import boto3
from time import time
import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from botocore.exceptions import ClientError
from datetime import datetime
import logging
from src.utils.constants import LOG_FOLDER_PATH, THRESHOLD_PLAYER_NUM_TO_RETURN, MAX_CACHE_SIZE
from src.tournament_data_utils.utils import get_all_sets_from_tournament_files, query_tournaments, download_s3_files
from src.smash_ranking import get_player_rating
from decimal import Decimal
from serverless_wsgi import handle_request  # WSGI adapter for Lambda
import uuid

app = Flask(__name__)
CORS(app)

os.makedirs(LOG_FOLDER_PATH, exist_ok=True)
log_file_name = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
log_file_path = os.path.join(LOG_FOLDER_PATH, log_file_name)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.StreamHandler(),                    # Console handler
                        logging.FileHandler(log_file_path, mode='a')  # File handler with append mode
                    ])

DEFAULT_START_DATE = '2018-07-16T00:00:00'
DEFAULT_END_DATE = '2024-11-06T00:00:00'
TIER_OPTIONS = ("P", "S+", "S", "A+", "A")

dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table("SmashRankingCache")


def md5_encode_key(data):
    """Encodes any Python object as an MD5 hash to use as a unique cache key.
       The hashing is order-independent for dictionaries and lists to ensure consistent keys.
    """
    # Recursive function to sort and serialize the input data
    def make_deterministic(obj):
        if isinstance(obj, dict):
            return {k: make_deterministic(v) for k, v in sorted(obj.items())}
        elif isinstance(obj, list):
            # If elements are dictionaries, convert each dictionary to a sorted tuple of items
            return sorted(
                make_deterministic(i) if not isinstance(i, dict) else tuple(sorted(i.items()))
                for i in obj
            )
        else:
            return obj

    # Make data deterministic and serialize to JSON
    deterministic_data = make_deterministic(data)
    serialized_data = json.dumps(deterministic_data, separators=(',', ':'), sort_keys=True)

    # Generate MD5 hash from serialized data
    return hashlib.md5(serialized_data.encode()).hexdigest()


def convert_floats_to_decimal(obj):
    """Recursively converts float values to Decimal"""
    if isinstance(obj, float):
        return Decimal(str(obj))
    elif isinstance(obj, dict):
        return {k: convert_floats_to_decimal(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_floats_to_decimal(i) for i in obj]
    return obj

def clean_empty_values(d):
    """Recursively remove empty strings, None values, and empty dictionaries"""
    if not isinstance(d, (dict, list)):
        return d
    if isinstance(d, list):
        return [v for v in (clean_empty_values(v) for v in d) if v is not None]
    return {k: v for k, v in ((k, clean_empty_values(v)) for k, v in d.items())
            if k and v is not None and v != "" and v != {}}


def store_in_cache(param_list, result):
    """Store item in cache with proper error handling"""
    cache_key = md5_encode_key(param_list)
    timestamp = int(time())

    try:
        # Convert all floats to Decimals
        decimal_result = convert_floats_to_decimal(result)

        # Create the item with converted values
        item = {
            'cache_key': cache_key,
            'result': decimal_result,
            'last_accessed': timestamp
        }

        # Clean any empty values that might cause DynamoDB validation errors
        cleaned_item = clean_empty_values(item)

        # Store in DynamoDB
        table.put_item(Item=cleaned_item)

        # Clean up old items if necessary
        response = table.scan(
            ProjectionExpression="cache_key,last_accessed",
            Select='SPECIFIC_ATTRIBUTES'
        )

        items = response['Items']
        if len(items) > MAX_CACHE_SIZE:
            # Sort by last_accessed timestamp
            items.sort(key=lambda x: x['last_accessed'])
            # Delete oldest items
            items_to_delete = items[:len(items) - MAX_CACHE_SIZE]

            with table.batch_writer() as batch:
                for item in items_to_delete:
                    batch.delete_item(Key={'cache_key': item['cache_key']})

    except ClientError as e:
        logging.error(f"Error storing item in cache: {str(e)}")
        logging.error(f"Attempted to store item: {cleaned_item}")
        raise


def get_from_cache(param_list):
    """Retrieve item from cache with proper error handling"""
    cache_key = md5_encode_key(param_list)

    try:
        response = table.get_item(
            Key={'cache_key': cache_key},
            ConsistentRead=True
        )

        item = response.get('Item')
        if item:
            # Update last_accessed timestamp
            timestamp = int(time())
            table.update_item(
                Key={'cache_key': cache_key},
                UpdateExpression="SET last_accessed = :timestamp",
                ExpressionAttributeValues={':timestamp': timestamp}
            )
            return item['result']
        return None

    except ClientError as e:
        logging.error(f"Error retrieving item from cache: {str(e)}")
        raise


def get_ranking_and_cache(ranking_to_run, tier_options, start_date, end_date, evaluation_level):
    queried_tournaments = query_tournaments(
        tier_options=tier_options,
        start_date=start_date,
        end_date=end_date
    )
    params = {"tier_options": tier_options, "ranking_to_run": ranking_to_run, "evaluation_level": evaluation_level, "tournament_list": ["{}-{}".format(result["tourney_slug"], result["event_slug"]) for result in queried_tournaments]}
    logging.info(f"Get rankings with: {params}")
    ratings_player_name_added = get_from_cache(params)
    if ratings_player_name_added is None:
        all_s3_files_to_download = ["{}-{}.json".format(result["tourney_slug"], result["event_slug"]) for result in queried_tournaments]
        download_s3_files(all_s3_files_to_download, overwrite=False)
        all_sets = get_all_sets_from_tournament_files(all_s3_files_to_download)
        ratings, id_to_player_name, player_to_id = get_player_rating(all_sets, ranking_to_run=ranking_to_run,
                                                                     evaluation_level="sets")
        result = {"ratings": sorted(ratings, key=lambda a: a["rating"], reverse=True)[:THRESHOLD_PLAYER_NUM_TO_RETURN], "id_to_player_name": id_to_player_name, "player_to_id": player_to_id}
        ratings_player_name_added = [
            {"player": id_to_player_name[r["player"]], "rating": r["rating"], "uncertainty": r["uncertainty"]} for r in
            result["ratings"]]
        store_in_cache(params, ratings_player_name_added)
    return ratings_player_name_added

@app.route('/get_ranking', methods=['GET'])
def get_ranking():
    # Extract parameters from the request
    logging.info("get_ranking called with:")
    logging.info("request.args:")
    logging.info(request.args)
    ranking_to_run = request.args.get('ranking_to_run')
    if ranking_to_run not in {"trueskill", "elo", "glicko2", "bradleyterry"}:
        return jsonify({"error": "Invalid ranking_to_run value"}), 400

    tier_options = request.args.get('tier_options', default=TIER_OPTIONS)
    tier_options = tuple(tier_options.split(',')) if isinstance(tier_options, str) else tier_options

    start_date = request.args.get('start_date', default=DEFAULT_START_DATE)
    end_date = request.args.get('end_date', default=DEFAULT_END_DATE)

    evaluation_level = request.args.get('evaluation_level')
    if evaluation_level not in {"sets", "games"}:
        return jsonify({"error": "Invalid evaluation_level value"}), 400

    try:
        # Ensure valid date format
        start_date = datetime.fromisoformat(start_date)
        end_date = datetime.fromisoformat(end_date)
    except ValueError:
        return jsonify({"error": "Invalid date format"}), 400

    # Call the get_ranking_and_cache function and return the result
    result = get_ranking_and_cache(ranking_to_run, tier_options, start_date.isoformat(), end_date.isoformat(), evaluation_level)
    return jsonify(result)

@app.route('/query_tournaments', methods=['GET'])
def query_tournaments_endpoint():
    logging.info("query_tournaments_endpoint called with:")
    logging.info("request.args:")
    logging.info(request.args)
    tier_options = request.args.get('tier_options', default=TIER_OPTIONS)
    tier_options = tuple(tier_options.split(',')) if isinstance(tier_options, str) else tier_options

    start_date = request.args.get('start_date', default=DEFAULT_START_DATE)
    end_date = request.args.get('end_date', default='2025-01-30T00:00:00')

    try:
        # Ensure valid date format
        start_date = datetime.fromisoformat(start_date)
        end_date = datetime.fromisoformat(end_date)
    except ValueError:
        return jsonify({"error": "Invalid date format"}), 400
    # Query tournaments
    tournaments = query_tournaments(tier_options=tier_options, start_date=start_date.isoformat(), end_date=end_date.isoformat())
    return jsonify(tournaments)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat()
    })

@app.before_request
def before_request():
    request.id = str(uuid.uuid4())
    g.start_time = time()

@app.after_request
def after_request(response):
    if hasattr(g, 'start_time'):
        elapsed = time() - g.start_time
        logging.info(f"Request {request.id} completed in {elapsed:.2f}s")
    return response

def lambda_handler(event, context):
    return handle_request(app, event, context)

# if __name__ == '__main__':
#     app.run(debug=True)