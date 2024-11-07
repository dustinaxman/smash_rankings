from boto3.dynamodb.conditions import Key, Attr
import json
import boto3
from src.utils.constants import tier_mapper, dynamo_db_table_name, s3_bucket, LOCAL_TOURNAMENT_DATA_DIR
#from concurrent.futures import ThreadPoolExecutor, as_completed
#from pathlib import Path

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
ddb_table = dynamodb.Table(dynamo_db_table_name)


def query_tournaments(tier_options=("P", "S+", "S", "A+", "A", "B+", "B", "C", "D"), start_date=None, end_date=None):
    """
    Query DynamoDB table for tournaments within a date range and specified tiers.

    Parameters:
        table_name (str): The DynamoDB table name.
        tier_options (tuple of str): Tuple of tier options to filter by (e.g., ('P', 'S')).
        start_date (str): Start date as an ISO 8601 string (e.g., '2023-01-01T00:00:00').
        end_date (str): End date as an ISO 8601 string (e.g., '2023-12-31T23:59:59').

    Returns:
        list: List of tournament items matching the criteria.
    """
    if tier_options is None:
        tier_options = ("P", "S+", "S", "A+", "A", "B+", "B", "C", "D")
    # Build the filter expression
    filter_expression = []
    expression_values = {}

    if tier_options:
        filter_expression.append(Attr('tier').is_in(tier_options))

    if start_date and end_date:
        filter_expression.append(Attr('date').between(start_date, end_date))

    # Combine filter expressions if both filters are present
    combined_expression = None
    if filter_expression:
        combined_expression = filter_expression[0]
        for expr in filter_expression[1:]:
            combined_expression = combined_expression & expr

    # Perform the scan with filter expressions
    response = ddb_table.scan(
        FilterExpression=combined_expression
    ) if combined_expression else ddb_table.scan()

    return response['Items']


def download_s3_files(all_s3_files_to_download, overwrite=False):
    """
    Download files from an S3 bucket to a local directory as quickly as possible.

    Parameters:
    - all_s3_files_to_download: List of file paths in S3 bucket.
    - s3_bucket: The name of the S3 bucket.
    - LOCAL_TOURNAMENT_DATA_DIR: Pathlib.Path object representing the local directory to download files into.
    - overwrite: Boolean, if True, overwrite existing files; if False, skip files that already exist.
    """
    # Ensure local directory exists
    LOCAL_TOURNAMENT_DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Download each file
    for s3_file in all_s3_files_to_download:
        local_file_path = LOCAL_TOURNAMENT_DATA_DIR / s3_file  # create full path for local file

        # Check if file exists locally and if overwrite is False, skip download
        if local_file_path.exists() and not overwrite:
            print(f"File {local_file_path} already exists and overwrite is set to False. Skipping download.")
            continue

        # Check if the file exists in S3 bucket
        try:
            s3.head_object(Bucket=s3_bucket, Key=s3_file)
        except s3.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                raise FileNotFoundError(f"The file {s3_file} does not exist in the bucket {s3_bucket}.")
            else:
                raise  # Re-raise the exception if it is not a 404 error

        # Download the file
        try:
            print(f"Downloading {s3_file} to {local_file_path}...")
            s3.download_file(s3_bucket, s3_file, str(local_file_path))
            print(f"Downloaded {s3_file} to {local_file_path}")
        except Exception as e:
            print(f"Error downloading {s3_file}: {e}")


def get_all_sets_from_tournament_files(all_tournament_files):
    all_sets = []
    for filename in all_tournament_files:
        with open(LOCAL_TOURNAMENT_DATA_DIR/filename, "r") as f:
            jsn = json.load(f)
            all_sets.extend([{"tournament_name": jsn["name"], "date": jsn["date"], **s} for s in jsn["sets"]])
    return all_sets


def get_all_sets_from_dates_and_tiers(tier_options=("P", "S+", "S", "A+", "A", "B+", "B", "C", "D"), start_date='2024-07-16T00:00:00', end_date='2024-10-30T00:00:00'):
    results = query_tournaments(
        tier_options=tier_options,
        start_date=start_date,
        end_date=end_date
    )
    all_s3_files_to_download = ["{}-{}.json".format(result["tourney_slug"], result["event_slug"]) for result in results]
    download_s3_files(all_s3_files_to_download, overwrite=False)
    all_sets = get_all_sets_from_tournament_files(all_s3_files_to_download)
    return all_sets


def display_rating(ratings_dict, threshold=100):
    rating_name = ratings_dict["name"]
    ratings = ratings_dict["ratings"]
    print(f"## {rating_name} Ratings")
    print("| Player | Mean Rating | Relative Uncertainty |")
    print("|--------|-------------|----------|")
    for record in sorted(ratings, key=lambda a: a["rating"], reverse=True)[:threshold]:
        player, rating, uncertainty = record["player"], record["rating"], record["uncertainty"]
        if uncertainty is not None:
            print(f"| {player} | {rating:.2f} | {uncertainty:.2f} |")
        else:
            print(f"| {player} | {rating:.2f} | None |")

