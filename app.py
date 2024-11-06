import hashlib
import boto3
from time import time
import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key
from datetime import datetime
import logging
from src.utils.constants import LOG_FOLDER_PATH, THRESHOLD_PLAYER_NUM_TO_RETURN, MAX_CACHE_SIZE
from src.tournament_data_utils.utils import get_all_sets_from_tournament_files, query_tournaments, download_s3_files
from src.smash_ranking import get_player_rating

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

def table_exists(table_name):
    try:
        dynamodb.Table(table_name).load()
        return True
    except ClientError:
        return False

def create_table(table_name):
    if not table_exists(table_name):
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[{'AttributeName': 'cache_key', 'KeyType': 'HASH'}, {'AttributeName': 'last_accessed', 'KeyType': 'RANGE'}],
            AttributeDefinitions=[{'AttributeName': 'cache_key', 'AttributeType': 'S'}, {'AttributeName': 'last_accessed', 'AttributeType': 'N'}],
            ProvisionedThroughput={'ReadCapacityUnits': 20, 'WriteCapacityUnits': 20}
        )
        table.wait_until_exists()
        logging.info(f"DynamoDB table '{table_name}' created.")


# Set up DynamoDB connection
dynamodb = boto3.resource("dynamodb")
create_table("SmashRankingCache")
table = dynamodb.Table("SmashRankingCache")

def md5_encode_key(data):
    """Encodes any Python object as an MD5 hash to use as a unique cache key.
       The hashing is order-independent for dictionaries and lists to ensure consistent keys.
    """

    # Recursive function to sort and serialize the input data
    def make_deterministic(obj):
        if isinstance(obj, dict):
            # Sort dictionaries by key and process values recursively
            return {k: make_deterministic(v) for k, v in sorted(obj.items())}
        elif isinstance(obj, list):
            # Sort lists and process elements recursively
            return sorted(make_deterministic(i) for i in obj)
        else:
            # Return other data types as-is
            return obj

    # Make data deterministic and serialize to JSON
    deterministic_data = make_deterministic(data)
    serialized_data = json.dumps(deterministic_data, separators=(',', ':'), sort_keys=True)

    # Generate MD5 hash from serialized data
    return hashlib.md5(serialized_data.encode()).hexdigest()


def store_in_cache(param_list, result):
    # Generate MD5 hash key from list of strings
    cache_key = md5_encode_key(param_list)

    # Set the current timestamp as the last_accessed time
    last_accessed = int(time())

    # Store the item in the cache
    table.put_item(Item={'cache_key': cache_key, 'result': result, 'last_accessed': last_accessed})

    # Check the number of items in the cache
    response = table.scan(ProjectionExpression="cache_key")
    item_count = len(response['Items'])

    # If we exceed the cache size, delete the oldest items
    if item_count > MAX_CACHE_SIZE:
        # Query for oldest items
        old_items = table.query(
            KeyConditionExpression=boto3.dynamodb.conditions.Key('cache_key').eq('cache') &
                                  boto3.dynamodb.conditions.Key('last_accessed').lt(last_accessed),
            Limit=item_count - MAX_CACHE_SIZE,
            ScanIndexForward=True  # Sort ascending (oldest first)
        )

        # Delete the oldest items
        with table.batch_writer() as batch:
            for item in old_items['Items']:
                batch.delete_item(Key={'cache_key': item['cache_key'], 'last_accessed': item['last_accessed']})

def get_from_cache(param_list):
    """Checks if an item exists in the cache. If found, returns the item and updates access time; otherwise, returns None."""
    # Generate MD5 hash key from list of strings
    cache_key = md5_encode_key(param_list)

    # Retrieve the item from the cache
    response = table.get_item(Key={'cache_key': cache_key})
    item = response.get('Item')

    if item:
        # Item found, update last_accessed timestamp
        last_accessed = int(time())
        table.update_item(
            Key={'cache_key': cache_key},
            UpdateExpression="SET last_accessed = :last_accessed",
            ExpressionAttributeValues={':last_accessed': last_accessed}
        )
        return item['result']
    else:
        # Item not found
        return None


def get_ranking_and_cache(ranking_to_run, tier_options, start_date, end_date, evaluation_level):
    queried_tournaments = query_tournaments(
        tier_options=tier_options,
        start_date=start_date,
        end_date=end_date
    )
    params = {"tier_options": tier_options, "ranking_to_run": ranking_to_run, "evaluation_level": evaluation_level, "tournament_list": ["{}-{}".format(result["tourney_slug"], result["event_slug"]) for result in queried_tournaments]}
    result = get_from_cache(params)
    if result is None:
        all_s3_files_to_download = ["{}-{}.json".format(result["tourney_slug"], result["event_slug"]) for result in queried_tournaments]
        download_s3_files(all_s3_files_to_download, overwrite=False)
        all_sets = get_all_sets_from_tournament_files(all_s3_files_to_download)
        ranking_to_run = "trueskill"
        ratings, id_to_player_name, player_to_id = get_player_rating(all_sets, ranking_to_run=ranking_to_run,
                                                                     evaluation_level="sets")
        result = {"ratings": ratings, "id_to_player_name": id_to_player_name, "player_to_id": player_to_id}
        store_in_cache(params, result)
    ratings = [
        {"player": id_to_player_name[r["player"]], "rating": r["rating"], "uncertainty": r["uncertainty"]} for r in
        result["ratings"]]
    return sorted(ratings, key=lambda a: a["rating"], reverse=True)[:THRESHOLD_PLAYER_NUM_TO_RETURN]

@app.route('/get_ranking', methods=['GET'])
def get_ranking():
    # Extract parameters from the request
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

if __name__ == '__main__':
    app.run(debug=True)