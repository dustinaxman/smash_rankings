from pathlib import Path
import os
import tempfile

LOCAL_TOURNAMENT_DATA_DIR = Path(os.path.join(tempfile.gettempdir(), "all_smash_tournament_data"))
LOG_FOLDER_PATH = os.path.join(tempfile.gettempdir(), "smash_tournament_logs")
THRESHOLD_PLAYER_NUM_TO_RETURN = 100
MAX_CACHE_SIZE = 10000
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

