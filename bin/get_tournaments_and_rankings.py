from src.tournament_data_utils.utils import get_all_sets_from_dates_and_tiers, display_rating, get_all_sets_from_tournament_files, query_tournaments, download_s3_files
from src.smash_ranking import get_player_rating
from time import time
from src.utils.constants import LOCAL_TOURNAMENT_DATA_DIR

#("P", "S+", "S", "A+", "A", "B+", "B", "C", "D")

all_sets = get_all_sets_from_dates_and_tiers(tier_options=("P", "S+", "S", "A+", "A"), start_date='2024-07-15T00:00:00', end_date='2024-10-30T00:00:00')
# ts = query_tournaments(tier_options=("P", "S+", "S", "A+", "A"), start_date='2021-06-16T00:00:00', end_date='2022-01-06T00:00:00')
# for t in ts:
#     print(t)
# # file_names = {file.name for file in LOCAL_TOURNAMENT_DATA_DIR.iterdir() if file.is_file()}
# # all_sets = get_all_sets_from_tournament_files(file_names)
# exit(1)

# glicko2
# elo
# trueskill
# bradleyterry

# file_names = {file.name for file in LOCAL_TOURNAMENT_DATA_DIR.iterdir() if file.is_file()}
#


# import cProfile
# import pstats
#
ranking_to_run = "simpleelo"
# start = time()
# cProfile.run('ratings, id_to_player_name, player_to_id = get_player_rating(all_sets, ranking_to_run=ranking_to_run, evaluation_level="sets")', 'output.prof')
ratings, id_to_player_name, player_to_id = get_player_rating(all_sets, ranking_to_run=ranking_to_run, evaluation_level="sets")
# print(time()-start)
# p = pstats.Stats('output.prof')
# p.sort_stats('cumulative').print_stats(10)
#
#
#
#
#
# # for k, v in id_to_player_name.items():
# #     if len(v) != 1:
# #         print(k, v)
#
ratings_dict = {"name": ranking_to_run, "ratings": [{"player": id_to_player_name[r["player"]], "rating": r["rating"], "uncertainty": r["uncertainty"]} for r in ratings]}
# #ratings_dict = {"name": ranking_to_run, "ratings": ratings}
display_rating(ratings_dict, threshold=100)

    # [{'event_slug': 'ultimate-singles',
    #   'date': '2024-02-16T18:00:00',
    #   'name': 'GENESIS X',
    #   'tourney_slug': 'genesis-x',
    #   'tier': 'P'},

# {
#   "player_1": "LG | Tweek",
#   "id_1": 12394650,
#   "score_1": 3,
#   "player_2": "Riddles",
#   "id_2": 12277894,
#   "score_2": 1,
#   "winner_id": 12394650
# },
