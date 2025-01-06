from src.tournament_data_utils.utils import get_all_sets_from_dates_and_tiers, display_rating, get_win_loss_interpretation, get_all_sets_from_tournament_files, query_tournaments, download_s3_files
from src.smash_ranking import get_player_rating
from src.smash_ranking import process_game_sets_to_simple_format
from time import time
import json
from src.utils.constants import LOCAL_TOURNAMENT_DATA_DIR

myrank_to_lumirank_name_mapping = {
    "ZETA | あcola": "acola",
    "FaZe | Sparg0": "Sparg0",
    "Sparg0": "Sparg0",
    "LG | Sonix": "Sonix",
    "FENNEL | ミーヤー/Miya": "Miya",
    "FENNEL | ミーヤー": "Miya",
    "FTG | ミーヤー": "Miya",
    "Moist | Light": "Light",
    "Sonix": "Sonix",
    "Zomba": "Zomba",
    "DTL | Syrup": "Syrup",
    "LG | Tweek": "Tweek",
    "Liquid | Riddles": "Riddles",
    "Riddles": "Riddles",
    "Solary | Glutonny": "Glutonny",
    "SST | Shuton": "Shuton",
    "RC | Shuton": "Shuton",
    "LG | MkLeo": "MkLeo",
    "Stride | Zomba": "Zomba",
    "LG | Zomba": "Zomba",
    "Revo | Yoshidora": "Yoshidora",
    "R2G | Kameme": "Kameme",
    "Liquid | Dabuz": "Dabuz",
    "ZETA | Tea": "Tea",
    "MSU | Onin": "Onin",
    "Onin": "Onin",
    "SZ | Asimo": "Asimo",
    "LG | Maister": "Maister",
    "DFM | zackray": "Zackray",
    "Kurama": "Kurama",
    "iXA | Yaura": "Yaura",
    "Stride | SHADIC": "SHADIC",
    "SHADIC": "SHADIC",
    "TW | スノー": "Snow",
    "E36 | Hurt": "Hurt",
    "Stride | MuteAce": "MuteAce",
    "26R | MuteAce": "MuteAce",
    "Lima": "Lima",
    "WIN | Lima": "Lima",
    "SOL | らる": "Raru",
    "AREA310 | ドラ右": "Doramigi",
    "Shory's | ShinyMark": "ShinyMark",
    "たまPだいふく": "TamaPDaifuku",
    "SBI | KEN": "KEN"
}

players_scores_2023_summer = {
    "acola": 100.0,
    "Sparg0": 98.51,
    "Miya": 87.31,
    "Sonix": 86.56,
    "Tweek": 84.76,
    "Light": 84.74,
    "MkLeo": 84.15,
    "Riddles": 79.56,
    "Shuton": 78.01,
    "Yoshidora": 76.97,
    "Glutonny": 75.99,
    "Kameme": 75.33,
    "Zomba": 75.25,
    "Tea": 74.37,
    "Asimo": 68.85,
    "MuteAce": 67.69,
    "Zackray": 67.26,
    "Maister": 66.65,
    "Yaura": 65.97,
    "Kurama": 64.77,
}

players_scores_2023 = {
    "acola": 100.00,
    "Sparg0": 97.85,
    "Sonix": 97.29,
    "Miya": 95.32,
    "Glutonny": 84.78,
    "Light": 84.46,
    "Tweek": 82.35,
    "Yoshidora": 80.89,
    "Riddles": 80.24,
    "Shuton": 79.75,
    "MkLeo": 79.32,
    "Tea": 79.11,
    "Kameme": 78.65,
    "Dabuz": 78.17,
    "Zomba": 77.62,
    "KEN": 76.05,
    "Asimo": 69.02,
    "Yaura": 68.34,
    "Hurt": 68.14,
    "MuteAce": 67.80,
}

players_scores_20241 = {
    "acola": 100.0,
    "Miya": 94.76,
    "Sonix": 91.23,
    "Hurt": 89.28,
    "Tweek": 84.67,
    "Shuton": 82.56,
    "SHADIC": 80.72,
    "TamaPDaifuku": 80.47,
    "Sparg0": 78.65,
    "Light": 78.02,
    "Raru": 77.81,
    "Doramigi": 76.80,
    "Yaura": 76.27,
    "Zomba": 74.96,
    "Asimo": 72.39,
    "Tea": 72.13,
    "MuteAce": 71.99,
    "Snow": 71.35,
    "ShinyMark": 71.05,
    "Zackray": 70.32,
}

players_scores_20242 = {
    "Sparg0": 100.0,
    "Miya": 99.05,
    "acola": 98.31,
    "Light": 92.30,
    "Sonix": 91.51,
    "Raru": 88.87,
    "Shuton": 88.86,
    "MkLeo": 87.59,
    "Asimo": 86.65,
    "Tweek": 86.53,
    "Zackray": 86.50,
    "Doramigi": 86.34,
    "Hurt": 82.37,
    "Glutonny": 81.25,
    "Syrup": 80.82,
    "Lima": 79.48,
    "SHADIC": 79.37,
    "Maister": 79.35,
    "Yoshidora": 78.93,
    "Snow": 76.94,
    "Kola": 76.86,
}


start_end = [
#['2019-02-01T00:00:00', '2019-07-08T00:00:00'],
#['2019-07-08T00:00:00', '2019-12-18T00:00:00'],
#['2022-01-01T00:00:00', '2022-12-30T00:00:00'],
['2022-12-19T00:00:00', '2023-07-23T00:00:00'], #summer 2023
['2022-12-14T00:00:00', '2023-12-18T00:00:00'], #2023
['2023-12-20T00:00:00', '2024-07-16T00:00:00'], #2024.1
['2024-07-16T00:00:00', '2024-11-30T00:00:00'] #2024.2
#['2018-07-16T00:00:00', '2024-11-30T00:00:00']
]


lumirank_ratings = [players_scores_2023_summer, players_scores_2023, players_scores_20241, players_scores_20242]



ranking_to_run = "elo"

#tier_weights = {"P": 1.5, "S+": 1.3, "S": 1.2, "A+": 1.1, "A": 0.9, "B+": 0.4, "B": 0.2}
#tier_weights = {"P": 1.3, "S+": 1.2, "S": 1.1, "A+": 1.1, "A": 1.0, "B+": 0.2, "B": 0.1}
#tier_weights = {"P": 2.0, "S+": 1.7, "S": 1.3, "A+": 1.2, "A": 1.0, "B+": 0.8, "B": 0.8}
#tier_weights = {"P": 2.0, "S+": 1.7, "S": 1.3, "A+": 1.2, "A": 1.0, "B+": 0.2, "B": 0.1} #GOOD!!
#tier_weights = {"P": 2.5, "S+": 2.1, "S": 1.8, "A+": 1.4, "A": 1.2, "B+": 0.2, "B": 0.1}
#tier_weights = {"P": 2.0, "S+": 1.7, "S": 1.3, "A+": 1.2, "A": 1.0, "B+": 0.8, "B": 0.7}
tier_weights = {"P": 1.4, "S+": 1.3, "S": 1.2, "A+": 1.1, "A": 1.0, "B+": 0.8, "B": 0.6}
import numpy as np

all_lumirank_players = set([k for lumirank_ratings_season in lumirank_ratings for k in lumirank_ratings_season])

for season_i, (start_date, end_date) in enumerate(start_end):
    lumirank_ratings_season = lumirank_ratings[season_i]
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
        {"player": id_to_player_name[r["player"]], "rating": (r["rating"]*A)+b, "uncertainty": r["uncertainty"], "lumirank": lumirank_ratings_season[myrank_to_lumirank_name_mapping[id_to_player_name[r["player"]]]] if ((id_to_player_name[r["player"]] in myrank_to_lumirank_name_mapping) and (myrank_to_lumirank_name_mapping[id_to_player_name[r["player"]]] in lumirank_ratings_season)) else None} for r in
        sorted_rankings if variance_thresh > r["uncertainty"]]}
    display_rating(ratings_dict, threshold=20)
#     for record in sorted(ratings_dict["ratings"], key=lambda a: a["rating"], reverse=True)[:20]:
#         print(record["player"])
#         record["rating"]
#         record["uncertainty"]
#         lumirank_player = myrank_to_lumirank_name_mapping[record["player"]]
#         lumirank_score = lumirank_ratings_season[lumirank_player]
#         # if record["player"] not in myrank_to_lumirank_name_mapping:
#         #     print("NOT IN myrank_to_lumirank_name_mapping", record["player"])
#         # if all([myrank_to_lumirank_name_mapping[record["player"]] not in l_rating for l_rating in lumirank_ratings]):
#         #     print("NOT IN LUMIRANK", myrank_to_lumirank_name_mapping[record["player"]])
#         # if myrank_to_lumirank_name_mapping[record["player"]] in all_lumirank_players:
#         #     all_lumirank_players.remove(myrank_to_lumirank_name_mapping[record["player"]])
#
#
# print(all_lumirank_players)

exit(1)


all_sets = get_all_sets_from_dates_and_tiers(tier_options=("P", "S+", "S", "A+", "A"), start_date=start_date,
                                             end_date=end_date)

simple_game_sets, id_to_player_name, player_to_id = process_game_sets_to_simple_format(all_sets, "sets", tournament_tier_weights=tier_weights)

top5 = set([
    "FaZe | Sparg0",
    "FENNEL | ミーヤー/Miya",
    "LG | Sonix",
    "ZETA | あcola",
    "Moist | Light"
])

top10 = set([
    "SOL | らる",
    "LG | MkLeo",
    "LG | Tweek",
    "SZ | Asimo",
    "RC | Shuton"
])

top20 = set([
    "Lima",
    "DFM | zackray",
    "AREA310 | ドラ右",
    "Zomba",
    "DTL | Syrup",
    "E36 | Hurt",
    "Liquid | Riddles",
    "LG | Maister",
    "SHADIC",
    "Revo | Yoshidora",
    "TW | スノー",
    "Moist | Kola",
    "SBI | KEN",
    "ZETA | Tea",
    "Solary | Glutonny",
])

from collections import defaultdict
all_players_with_good_wins = defaultdict(lambda: defaultdict(list))

#print(all_sets[:10])

for player1, player2, score1, score2, weight in simple_game_sets:
    if id_to_player_name[player1] in top5 and score2 > score1:
        all_players_with_good_wins[player2]["top5"].append(player1)
    if id_to_player_name[player2] in top5 and score1 > score2:
        all_players_with_good_wins[player1]["top5"].append(player2)
    if id_to_player_name[player1] in top10 and score2 > score1:
        all_players_with_good_wins[player2]["top10"].append(player1)
    if id_to_player_name[player2] in top10 and score1 > score2:
        all_players_with_good_wins[player1]["top10"].append(player2)
    if id_to_player_name[player1] in top20 and score2 > score1:
        all_players_with_good_wins[player2]["top20"].append(player1)
    if id_to_player_name[player2] in top20 and score1 > score2:
        all_players_with_good_wins[player1]["top20"].append(player2)

for player, top_dicts in sorted(all_players_with_good_wins.items(), key=lambda a: 1.5*len(a[1]["top5"]) + len(a[1]["top10"]) + 0.5*len(a[1]["top10"]), reverse=True):
    if len(top_dicts["top5"]) > 1 or len(top_dicts["top10"]) > 2:
        print(id_to_player_name[player])
        print("TOP5:", ", ".join([id_to_player_name[p] for p in top_dicts["top5"]]))
        print("TOP10:", ", ".join([id_to_player_name[p] for p in top_dicts["top10"]]))
        print("TOP20:", ", ".join([id_to_player_name[p] for p in top_dicts["top20"]]))
        print("#################")











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
