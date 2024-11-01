from pathlib import Path

LOCAL_TOURNAMENT_DATA_DIR = Path.home()/"all_smash_tournament_data"
LOG_FOLDER_PATH = str(Path.home()/"smash_tournament_logs")

s3_bucket = 'smash-ranking-tournament-data'
dynamo_db_table_name = 'smash-ranking-tournament-table'

tier_mapper = {
    '6': 'P',
    '5+': 'S+',
    '5': 'S',
    '4+': 'A+',
    '4': 'A',
    '3+': 'B+',
    '3': 'B',
    '2': 'C',
    '1': 'D'
}

