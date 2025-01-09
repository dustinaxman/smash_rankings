from boto3.dynamodb.conditions import Key, Attr
import json
import boto3
from src.utils.constants import tier_mapper, dynamo_db_table_name, s3_bucket, LOCAL_TOURNAMENT_DATA_DIR, LOG_FOLDER_PATH
from concurrent.futures import ThreadPoolExecutor, as_completed
import multiprocessing
from botocore.config import Config
import logging
import os
from datetime import datetime

# Increase the max connections in the connection pool
config = Config(max_pool_connections=50)

# Initialize S3 client with custom config
s3 = boto3.client('s3', config=config)

dynamodb = boto3.resource('dynamodb')
ddb_table = dynamodb.Table(dynamo_db_table_name)

# os.makedirs(LOG_FOLDER_PATH, exist_ok=True)
# log_file_name = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
# log_file_path = os.path.join(LOG_FOLDER_PATH, log_file_name)

# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s - %(levelname)s - %(message)s',
#                     handlers=[
#                         logging.StreamHandler(),                    # Console handler
#                         logging.FileHandler(log_file_path, mode='a')  # File handler with append mode
#                     ])

logger = logging.getLogger()
logger.setLevel(logging.INFO)

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
    logger.info(f"Calling query_tournaments with: {tier_options}, {start_date}, {end_date}")
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
    return sorted(response['Items'], key=lambda x: x['date'], reverse=True)


def download_single_file(s3_bucket, s3_file, local_file_path, overwrite):
    """Helper function to download a single file from S3."""
    if local_file_path.exists() and not overwrite:
        return f"Skipped {s3_file}, already exists."

    try:
        s3.download_file(s3_bucket, s3_file, str(local_file_path))
        return f"Downloaded {s3_file} to {local_file_path}"
    except Exception as e:
        return f"Error downloading {s3_file}: {e}"


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
    if len(all_s3_files_to_download) == 0:
        return
    # Define maximum threads
    num_cores = multiprocessing.cpu_count()
    max_threads = min(4 * num_cores, len(all_s3_files_to_download))

    # Use ThreadPoolExecutor to download files in parallel
    with ThreadPoolExecutor(max_threads) as executor:
        future_to_file = {
            executor.submit(download_single_file, s3_bucket, s3_file, LOCAL_TOURNAMENT_DATA_DIR / s3_file,
                            overwrite): s3_file
            for s3_file in all_s3_files_to_download
        }

        # Process completed downloads
        for future in as_completed(future_to_file):
            s3_file = future_to_file[future]
            try:
                logger.info(future.result())
            except Exception as e:
                logger.info(f"Error with file {s3_file}: {e}")

def get_all_sets_from_tournament_files(all_tournament_files):
    all_sets = []
    for filename in all_tournament_files:
        with open(LOCAL_TOURNAMENT_DATA_DIR/filename, "r") as f:
            jsn = json.load(f)
            all_sets.extend([{"tournament_name": jsn["name"], "date": jsn["date"], "tier": jsn["tier"], **s} for s in jsn["sets"]])
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
    print("| Rank | Player | Mean Rating | Relative Uncertainty |")
    print("|---|--------|-------------|----------|")
    for rank, record in enumerate(sorted(ratings, key=lambda a: a["rating"], reverse=True)[:threshold]):
        player, rating, uncertainty = record["player"], record["rating"], record["uncertainty"]
        player = player.replace("|", " ")
        if "lumirank" not in record:
            if uncertainty is not None:
                print(f"| {rank} | {player} | {rating:.4f} | {uncertainty:.2f} |")
            else:
                print(f"| {rank} | {player} | {rating:.4f} | None |")
        else:
            lumirank = record["lumirank"] if record["lumirank"] is not None else 0
            lumirank_diff = 100 if lumirank is None else rating-lumirank
            if uncertainty is not None:
                print(f"| {rank} | {player} | {rating:.4f} | {uncertainty:.2f} | {lumirank:.2f} | {lumirank_diff:.2f}")
            else:
                print(f"| {rank} | {player} | {rating:.4f} | None | {lumirank:.2f} | {lumirank:.2f} | {lumirank_diff:.2f}")


def get_win_loss_interpretation(ratings, top_win_loss_record, id_to_player_name):
    sorted_rankings = sorted(ratings, key=lambda a: a["rating"], reverse=True)
    player_to_rank = {}
    for i, r in enumerate(sorted_rankings):
        player_to_rank[r["player"]] = i + 1

    top_players = [r["player"] for r in sorted_rankings[:25]]

    top_win_loss_record_merged = {}

    for player1 in top_players:
        top_win_loss_record_merged[player1] = {}
        for player2, winloss_record in top_win_loss_record[player1].items():
            matchup_count_win, p1_update_win = winloss_record["win"]
            matchup_count_loss, p1_update_loss = winloss_record["loss"]

            if player_to_rank[player2] > 100:
                record = top_win_loss_record_merged[player1].setdefault("UNRANKED", {"win": [0, 0], "loss": [0, 0]})
                record["win"][0] += matchup_count_win
                record["win"][1] += p1_update_win
                record["loss"][0] += matchup_count_loss
                record["loss"][1] += p1_update_loss
            else:
                top_win_loss_record_merged[player1][player2] = {
                    "win": [matchup_count_win, p1_update_win],
                    "loss": [matchup_count_loss, p1_update_loss],
                }

    player_win_loss_interpretation = []
    player_totals = {
        player1: sum(
            record["win"][1] + record["loss"][1] for record in matchups.values()
        )
        for player1, matchups in top_win_loss_record_merged.items()
    }

    for player1 in sorted(player_totals, key=player_totals.get, reverse=True):
        total_for_player = player_totals[player1]
        matchups = top_win_loss_record_merged[player1]
        all_wins_and_losses = []

        for player2, record in matchups.items():
            name = id_to_player_name.get(player2, "UNRANKED") if player2 != "UNRANKED" else "UNRANKED"
            rank = player_to_rank.get(player2, "UNRANKED") if player2 != "UNRANKED" else "UNRANKED"

            if record["win"][0] > 0:
                all_wins_and_losses.append(
                    {"player_id": player2, "player_name": name, "player_rank": rank, "win_count": record["win"][0], "score": record["win"][1]}
                )
            if record["loss"][0] > 0:
                all_wins_and_losses.append(
                    {"player_id": player2, "player_name": name, "player_rank": rank, "loss_count": record["loss"][0], "score": record["loss"][1]}
                )

        all_wins_and_losses.sort(key=lambda x: abs(x["score"]), reverse=True)
        player_win_loss_interpretation.append(
            {"player_id": player1, "player_name": id_to_player_name[player1], "total_for_player": total_for_player, "all_wins_and_losses": all_wins_and_losses}
        )
    return player_win_loss_interpretation





# top_win_loss_record_merged = defaultdict(lambda: defaultdict(lambda: {"win": [0, 0], "loss": [0, 0]}))
# for player1 in top_players:
#     for player2, winloss_record in top_win_loss_record[player1].items():
#         matchup_count_loss, p1_update_loss = winloss_record["loss"]
#         matchup_count_win, p1_update_win = winloss_record["win"]
#         if player_to_rank[player2] > 100:
#             top_win_loss_record_merged[player1]["UNRANKED"]["win"][0] += matchup_count_win
#             top_win_loss_record_merged[player1]["UNRANKED"]["win"][1] += p1_update_win
#         else:
#             top_win_loss_record_merged[player1][player2]["win"][0] = matchup_count_win
#             top_win_loss_record_merged[player1][player2]["win"][1] = p1_update_win
#         top_win_loss_record_merged[player1][player2]["loss"][0] = matchup_count_loss
#         top_win_loss_record_merged[player1][player2]["loss"][1] = p1_update_loss
#
# player_win_loss_interpretation = []
# for player1, matchups_dict in sorted(top_win_loss_record_merged.items(), key = lambda a: sum([a[1][p2]["win"][1] for p2 in a[1]]) + sum([a[1][p2]["loss"][1] for p2 in a[1]]), reverse=True):
#     total_for_player = sum([top_win_loss_record_merged[player1][p2]["win"][1] for p2 in top_win_loss_record_merged[player1]]) + sum([top_win_loss_record_merged[player1][p2]["loss"][1] for p2 in top_win_loss_record_merged[player1]])
#     all_wins_and_losses = []
#     for player2 in top_win_loss_record_merged[player1]:
#         if top_win_loss_record_merged[player1][player2]["win"][0] > 0:
#             all_wins_and_losses.append((player2, id_to_player_name[player2] if player2 != "UNRANKED" else "UNRANKED", player_to_rank[player2] if player2 != "UNRANKED" else "UNRANKED", "wins", top_win_loss_record_merged[player1][player2]["win"][0], top_win_loss_record_merged[player1][player2]["win"][1]))
#         if top_win_loss_record_merged[player1][player2]["loss"][0] > 0:
#             all_wins_and_losses.append((player2, id_to_player_name[player2] if player2 != "UNRANKED" else "UNRANKED", player_to_rank[player2] if player2 != "UNRANKED" else "UNRANKED", "losses", top_win_loss_record_merged[player1][player2]["loss"][0], top_win_loss_record_merged[player1][player2]["loss"][1]))
#     player_win_loss_interpretation.append((player1, total_for_player, sorted(all_wins_and_losses, key=lambda a: abs(a[5]), reverse=True)))
#
