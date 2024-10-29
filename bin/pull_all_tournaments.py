from src.smash_data.puller import process_tournaments
TOURNAMENT_FOLDER_PATH = "/Users/deaxman/Downloads/all_smash_rankings/"
excluded_tiers = ("D", "C", "B", "B+", "A", "A+", "S", "S+")

process_tournaments(google_sheets_url=None, sheet_name=None, tournament_folder_path=TOURNAMENT_FOLDER_PATH, excluded_tiers=excluded_tiers)
