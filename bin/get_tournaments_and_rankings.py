from src.tournament_data_utils.utils import get_all_sets_from_dates_and_tiers, display_rating
from src.smash_ranking import get_player_rating

#("P", "S+", "S", "A+", "A", "B+", "B", "C", "D")

all_sets = get_all_sets_from_dates_and_tiers(tier_options=("P", "S+", "S", "A+", "A", "B+", "B"), start_date='2019-07-16T00:00:00', end_date='2024-10-30T00:00:00')

ranking_to_run = "elo"
ratings, id_to_player_name, player_to_id = get_player_rating(all_sets, ranking_to_run=ranking_to_run, evaluation_level="sets")

for k, v in id_to_player_name.items():
    if len(v) != 1:
        print(k, v)

#ratings_dict = {"name": ranking_to_run, "ratings": [{"player": list(id_to_player_name[int(r["player"])])[0], "rating": r["rating"], "variance": r["variance"]} for r in ratings]}
ratings_dict = {"name": ranking_to_run, "ratings": ratings}

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
