from src.tournament_data_utils.utils import get_all_sets_from_dates_and_tiers, display_rating, get_all_sets_from_tournament_files, query_tournaments, download_s3_files
from src.smash_ranking import get_player_rating
from time import time
from src.utils.constants import LOCAL_TOURNAMENT_DATA_DIR

#("P", "S+", "S", "A+", "A", "B+", "B", "C", "D")
print("DOGS")
#all_sets = get_all_sets_from_dates_and_tiers(tier_options=("P", "S+", "S", "A+", "A", "B+", "B", "C"), start_date='2018-01-01T00:00:00', end_date='2025-01-01T00:00:00')
#all_sets = get_all_sets_from_dates_and_tiers(tier_options=("P", "S+", "S", "A+", "A", "B+", "B"), start_date='2023-01-01T00:00:00', end_date='2024-01-01T00:00:00')


all_sets = get_all_sets_from_dates_and_tiers(tier_options=("P", "S+", "S", "A+", "A", "B+", "B"), start_date='2024-01-01T00:00:00', end_date='2024-07-15T00:00:00')

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
print("CATS")
# import cProfile
# import pstats
#
ranking_to_run = "elo"
# start = time()
# cProfile.run('ratings, id_to_player_name, player_to_id = get_player_rating(all_sets, ranking_to_run=ranking_to_run, evaluation_level="sets")', 'output.prof')
start = time()
ratings, id_to_player_name, player_to_id, top_win_loss_record = get_player_rating(all_sets, ranking_to_run=ranking_to_run, evaluation_level="sets")
print(time() - start)
top_win_loss_record = top_win_loss_record.items()
top_win_loss_record_merged = []
for p, r in top_win_loss_record:
    new_r = []
    pid_winloss_to_total_score = defaultdict(lambda: [int(0), float(0.0)])
    for p2, winloss, score in r:
        if p2 == "UNRANKED" and winloss == "loss":
            new_r.append((p2, winloss, 1, score))
        else:
            pid_winloss_to_total_score[(p2, winloss)][1] += score
            pid_winloss_to_total_score[(p2, winloss)][0] += 1
    for (p2, winloss), (total_count, total_score) in pid_winloss_to_total_score.items():
        new_r.append((p2, winloss, total_count, total_score))
    top_win_loss_record_merged.append((p, new_r))
for player, records in sorted(top_win_loss_record_merged, key=lambda a: sum([s[3] for s in a[1]]), reverse=True)[:10]:
    if True or "ミーヤー" in id_to_player_name[player] or "cola" in id_to_player_name[player]:
        print(player, id_to_player_name[player], sum([s[3] for s in records]))
        for p in [(r[0], id_to_player_name[r[0]] if r[0] != "UNRANKED" else "UNRANKED", r[1], r[2], r[3]) for r in sorted(records, key=lambda a: abs(a[3]), reverse=True)]:
            print(p)
        print("")
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
display_rating(ratings_dict, threshold=200)

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
