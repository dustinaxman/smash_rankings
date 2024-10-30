from src.tournament_data_utils.utils import get_all_sets_from_dates_and_tiers, display_rating
from src.smash_ranking import get_player_rating

#("P", "S+", "S", "A+", "A", "B+", "B", "C", "D")

all_sets = get_all_sets_from_dates_and_tiers(tier_options=("P", "S+", "S", "A+", "A", "B+", "B"), start_date='2024-07-16T00:00:00', end_date='2024-10-30T00:00:00')

ratings = get_player_rating(all_sets, ranking_to_run="elo", evaluation_level="sets")


display_rating(ratings, threshold=100)

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
