import argparse
import time
from src.smash_data.puller import process_tournaments
import boto3


dynamodb = boto3.client('dynamodb')

def get_google_sheets_url_from_dynamodb():
    response = dynamodb.get_item(
        TableName='smash-tournaments-tracker-info',
        Key={'ID': {'S': 'tournament_info'}}
    )

    item = response.get('Item', {})
    google_sheets_url = item.get('google_sheets_url', {}).get('S')
    google_sheets_sheetname = item.get('sheet_name', {}).get('S')
    return google_sheets_url, google_sheets_sheetname


def main():
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Process tournaments data.")
    parser.add_argument(
        '--tournament_folder_path',
        type=str,
        help='Path to the tournament folder. If not provided, defaults to using google_sheets_url from DynamoDB.'
    )
    args = parser.parse_args()

    # Get google_sheets_url if tournament_folder_path is not provided
    tournament_folder_path = args.tournament_folder_path
    google_sheets_url = None

    if tournament_folder_path is None:
        google_sheets_url, google_sheets_sheetname = get_google_sheets_url_from_dynamodb()

    excluded_tiers = ()
    start = time.time()
    process_tournaments(
        google_sheets_url=google_sheets_url,
        sheet_name=google_sheets_sheetname,
        tournament_folder_path=tournament_folder_path,
        excluded_tiers=excluded_tiers
    )
    print(f"Processing time: {time.time() - start:.2f} seconds")

if __name__ == "__main__":
    main()
# '6': 'P',
#     '5+': 'S+',
#     '5': 'S',
#     '4+': 'A+',
#     '4': 'A',
#     '3+': 'B+',
#     '3': 'B',
#     '2': 'C',
#     '1': 'D'