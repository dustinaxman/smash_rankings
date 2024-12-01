from src.tournament_data_utils.utils import get_all_sets_from_dates_and_tiers, display_rating, get_win_loss_interpretation, get_all_sets_from_tournament_files, query_tournaments, download_s3_files
from src.smash_ranking import get_player_rating
from time import time
import json
from src.utils.constants import LOCAL_TOURNAMENT_DATA_DIR

start_end = [
#['2019-02-01T00:00:00', '2019-07-08T00:00:00'],
#['2019-07-08T00:00:00', '2019-12-18T00:00:00'],
#['2022-01-01T00:00:00', '2022-12-30T00:00:00'],
#['2022-12-14T00:00:00', '2023-12-18T00:00:00'],
#['2023-12-20T00:00:00', '2024-07-16T00:00:00'],
#['2024-07-16T00:00:00', '2024-11-30T00:00:00']
['2018-07-16T00:00:00', '2024-11-30T00:00:00']
]

ranking_to_run = "elo"

#tier_weights = {"P": 1.5, "S+": 1.3, "S": 1.2, "A+": 1.1, "A": 0.9, "B+": 0.4, "B": 0.2}
#tier_weights = {"P": 1.3, "S+": 1.2, "S": 1.1, "A+": 1.1, "A": 1.0, "B+": 0.2, "B": 0.1}
#tier_weights = {"P": 2.0, "S+": 1.7, "S": 1.3, "A+": 1.2, "A": 1.0, "B+": 0.8, "B": 0.8}
#tier_weights = {"P": 2.0, "S+": 1.7, "S": 1.3, "A+": 1.2, "A": 1.0, "B+": 0.2, "B": 0.1} #GOOD!!
tier_weights = {"P": 2.0, "S+": 1.7, "S": 1.3, "A+": 1.2, "A": 1.0, "B+": 0.2, "B": 0.1}
import numpy as np

for start_date, end_date in start_end:
	# create overall dict (overall_rankings) that will be the mean normalized score of the top 100 of sorted_rankings across all tiers/weights
	all_sets = get_all_sets_from_dates_and_tiers(tier_options=("P", "S+", "S", "A+", "A", "B+", "B"), start_date=start_date, end_date=end_date)
	ratings, id_to_player_name, player_to_id, top_win_loss_record = get_player_rating(all_sets, ranking_to_run=ranking_to_run, evaluation_level="sets", tournament_tier_weights=tier_weights)
	sorted_rankings = sorted(ratings, key=lambda a: a["rating"], reverse=True)[:100]
	#normalize the ratings
	#add to overall_rankings dict but with the rating score being weighted by "weight" variable
	variance_thresh = np.mean([r["uncertainty"] for r in sorted_rankings]) * 3
	print("mean", np.mean([r["uncertainty"] for r in sorted_rankings]))
	max_score = np.max([r["rating"] for r in sorted_rankings])
	score_50 = sorted([r["rating"] for r in sorted_rankings], reverse=True)[49]
	A = 50.0/float(max_score-score_50)
	b = 100.0-(A*max_score)
	ratings_dict = {"name": ranking_to_run, "ratings": [
		{"player": id_to_player_name[r["player"]], "rating": (r["rating"]*A)+b, "uncertainty": r["uncertainty"]} for r in
		sorted_rankings if variance_thresh > r["uncertainty"]]}
	display_rating(ratings_dict, threshold=50)
















#("P", "S+", "S", "A+", "A", "B+", "B", "C", "D")
#print("DOGS")
#all_sets = get_all_sets_from_dates_and_tiers(tier_options=("P", "S+", "S", "A+", "A", "B+", "B", "C"), start_date='2018-01-01T00:00:00', end_date='2025-01-01T00:00:00')
#all_sets = get_all_sets_from_dates_and_tiers(tier_options=("P", "S+", "S", "A+", "A", "B+", "B"), start_date='2023-01-01T00:00:00', end_date='2024-01-01T00:00:00')


#all_sets = get_all_sets_from_dates_and_tiers(tier_options=("P", "S+", "S", "A+", "A", "B+"), start_date='2024-07-15T00:00:00', end_date='2024-11-19T00:00:00')

#all_sets = get_all_sets_from_dates_and_tiers(tier_options=("P", "S+", "S", "A+", "A"), start_date='2023-03-10T00:00:00', end_date='2023-06-01T00:00:00')


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

from collections import defaultdict
# print("CATS")
# # import cProfile
# # import pstats
# #
# ranking_to_run = "elo"
# # start = time()
# # cProfile.run('ratings, id_to_player_name, player_to_id = get_player_rating(all_sets, ranking_to_run=ranking_to_run, evaluation_level="sets")', 'output.prof')
# start = time()
# ratings, id_to_player_name, player_to_id, top_win_loss_record = get_player_rating(all_sets, ranking_to_run=ranking_to_run, evaluation_level="sets")
#
# print(time()-start)
# print("WAT")
#
# sorted_rankings = sorted(ratings, key=lambda a: a["rating"], reverse=True)

# player_win_loss_interpretation = get_win_loss_interpretation(ratings, top_win_loss_record, id_to_player_name)
#
# print("dustin", time()-start)



# for p1_info in player_win_loss_interpretation:
#     print(p1_info["player_name"], p1_info["total_for_player"])
#     for winloss_info in p1_info["all_wins_and_losses"]:
#         print(json.dumps(winloss_info))


# for player_1_dict in player_win_loss_interpretation:
#     print(player_1_dict)


#print(time()-start)
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
# ratings_dict = {"name": ranking_to_run, "ratings": [{"player": id_to_player_name[r["player"]], "rating": r["rating"], "uncertainty": r["uncertainty"]} for r in ratings]}
# # #ratings_dict = {"name": ranking_to_run, "ratings": ratings}
# display_rating(ratings_dict, threshold=50)

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
