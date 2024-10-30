from src.smash_data.puller import process_tournaments
import time
TOURNAMENT_FOLDER_PATH = "/Users/deaxman/Downloads/all_smash_rankings/"
excluded_tiers = ("D", "C")
start = time.time()
process_tournaments(google_sheets_url=None, sheet_name=None, tournament_folder_path=TOURNAMENT_FOLDER_PATH, excluded_tiers=excluded_tiers)
print(time.time() - start)

# '6': 'P',
#     '5+': 'S+',
#     '5': 'S',
#     '4+': 'A+',
#     '4': 'A',
#     '3+': 'B+',
#     '3': 'B',
#     '2': 'C',
#     '1': 'D'