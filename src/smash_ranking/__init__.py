import trueskill as ts
from collections import defaultdict
import choix

# def process_game_sets_to_simple_format(game_sets, evaluation_level):
#     simple_game_sets = []
#     id_to_player_name = defaultdict(set)
#     player_to_id = defaultdict(set)
#     for game_set in game_sets:
#         player_1_name = game_set["player_1"]
#         player_2_name = game_set["player_2"]
#         player_1_id = game_set["id_1"]
#         player_2_id = game_set["id_2"]
#         player1_uniq_representation = f"{player_1_id}"
#         player2_uniq_representation = f"{player_2_id}"
#         if evaluation_level == "games":
#             score1 = game_set["score_1"]
#             score2 = game_set["score_2"]
#             score1 = 0 if score1 is None else score1
#             score2 = 0 if score2 is None else score2
#             if (score1 == 0 and score2 == 0) or score1 < 0 or score2 < 0:
#                 continue
#         elif evaluation_level == "sets":
#             score1 = 1 if player_1_id == game_set["winner_id"] else 0
#             score2 = 1 if player_2_id == game_set["winner_id"] else 0
#         id_to_player_name[player_1_id].add(player_1_name)
#         id_to_player_name[player_2_id].add(player_2_name)
#         player_to_id[player_1_name].add(player_1_id)
#         player_to_id[player_2_name].add(player_2_id)
#         #very simple code to find first example of two sets where the same player has multiple different ids.  Print out both game_set dicts
#         simple_game_sets.append([player1_uniq_representation, player2_uniq_representation, score1, score2])
#     return simple_game_sets, id_to_player_name, player_to_id

def process_game_sets_to_simple_format(game_sets, evaluation_level):
    simple_game_sets = []
    id_to_player_name = defaultdict(set)
    player_to_id = defaultdict(set)
    found_inconsistent_example = False  # Flag to stop after finding the first inconsistency

    for game_set in game_sets:
        player_1_name = str(game_set["player_1"])
        player_2_name = str(game_set["player_2"])
        player_1_id = int(game_set["id_1"])
        player_2_id = int(game_set["id_2"])
        player1_uniq_representation = f"{player_1_name}"
        player2_uniq_representation = f"{player_2_name}"
        if game_set["score_1"] is None or game_set["score_2"] is None:
            continue
        if (game_set["score_1"] == 0 and game_set["score_2"] == 0) or game_set["score_1"] < 0 or game_set["score_2"] < 0:
            continue
        if evaluation_level == "games":
            score1 = game_set["score_1"]
            score2 = game_set["score_2"]
            score1 = 0 if score1 is None else score1
            score2 = 0 if score2 is None else score2
            if (score1 == 0 and score2 == 0) or score1 < 0 or score2 < 0:
                continue
        elif evaluation_level == "sets":
            score1 = 1 if player_1_id == game_set["winner_id"] else 0
            score2 = 1 if player_2_id == game_set["winner_id"] else 0

        # Track player name and ID associations
        id_to_player_name[player_1_id].add(player_1_name)
        id_to_player_name[player_2_id].add(player_2_name)
        player_to_id[player_1_name].add(player_1_id)
        player_to_id[player_2_name].add(player_2_id)


        # Very simple code to find the first example of two sets where the same player has multiple different IDs
        # Print out both `game_set` dictionaries
        # if not found_inconsistent_example:
        #     for player_name, ids in player_to_id.items():
        #         if len(ids) > 1:  # If the player has more than one unique ID
        #             # Find two sets with different IDs for the same player
        #             print(player_name, ids)
        #             conflicting_sets = [
        #                 gs for gs in game_sets if (gs["player_1"] == player_name and gs["id_1"] in ids) or
        #                                           (gs["player_2"] == player_name and gs["id_2"] in ids)
        #             ]
        #             dogs = [
        #                 gs for gs in game_sets if (gs["id_1"] == 18118445) or
        #                                           (gs["id_2"] == 18118445)
        #             ]
        #             print(dogs[0]["player_1"] == player_name)
        #
        #             if len(conflicting_sets) >= 2:
        #                 print("Example sets with inconsistent IDs for player:", player_name)
        #                 print(conflicting_sets)
        #                 print(conflicting_sets[1])
        #                 print("what")
        #                 print(dogs)
        #                 found_inconsistent_example = True
        #                 break

        simple_game_sets.append([player1_uniq_representation, player2_uniq_representation, score1, score2])

    return simple_game_sets, id_to_player_name, player_to_id


def run_bradley_terry(simple_game_sets):
    comparisons = []
    for player1, player2, score1, score2 in simple_game_sets:
        comparisons += [(player1, player2)] * int(score1)
        comparisons += [(player2, player1)] * int(score2)

    # Map players to indices
    players = list(set([p for match in simple_game_sets for p in match[:2]]))
    player_idx = {p: i for i, p in enumerate(players)}

    # Convert comparisons to numeric indices
    comparisons_numeric = [(player_idx[p1], player_idx[p2]) for p1, p2 in comparisons]

    # Fit Bradley-Terry model
    bt_ratings = choix.ilsr_pairwise(len(players), comparisons_numeric)
    ratings = [{"player": p, "rating": r, "variance": None} for p, r in zip(players, bt_ratings)]
    return ratings


def run_elo(simple_game_sets):
    elo_ratings = defaultdict(lambda: 1200)  # Default initial rating of 1200
    games_played = defaultdict(int)  # Track total games played per player

    for matchup in simple_game_sets:
        player1, player2, score1, score2 = matchup
        total_games = score1 + score2
        if total_games == 0:
            continue

        games_played[player1] += total_games
        games_played[player2] += total_games

        # Determine if players are provisional based on games played
        is_provisional1 = games_played[player1] < 20
        is_provisional2 = games_played[player2] < 20

        # Skip Elo adjustment for established players facing provisional opponents
        if not is_provisional1 and is_provisional2:
            continue
        if not is_provisional2 and is_provisional1:
            continue

        # Set K-factor based on experience and rating
        def get_k_factor(player):
            if games_played[player] < 30:  # Provisional player
                return 40
            elif elo_ratings[player] >= 2400:  # Top player
                return 10
            else:  # Established player
                return 20

        k_factor1 = get_k_factor(player1)
        k_factor2 = get_k_factor(player2)

        # Calculate expected scores for both players
        expected_score1 = 1 / (1 + 10 ** ((elo_ratings[player2] - elo_ratings[player1]) / 400))
        expected_score2 = 1 - expected_score1

        # Calculate actual scores as proportions
        actual_score1 = score1 / total_games
        actual_score2 = score2 / total_games

        # Update ratings based on K-factors and actual vs expected scores
        elo_ratings[player1] += k_factor1 * (actual_score1 - expected_score1)
        elo_ratings[player2] += k_factor2 * (actual_score2 - expected_score2)

    # Prepare results in desired format
    ratings = [{"player": player, "rating": rating, "variance": None} for player, rating in elo_ratings.items()]
    return ratings

def run_trueskill(simple_game_sets):
    env = ts.TrueSkill()
    ts_ratings = defaultdict(lambda: env.create_rating())
    for matchup in simple_game_sets:
        player1, player2, score1, score2 = matchup
        total_games = score1 + score2
        if total_games == 0:
            return
        if score1 > score2:
            new_rating1, new_rating2 = env.rate_1vs1(ts_ratings[player1], ts_ratings[player2])
        elif score2 > score1:
            new_rating2, new_rating1 = env.rate_1vs1(ts_ratings[player2], ts_ratings[player1])
        else:
            new_rating1, new_rating2 = env.rate_1vs1(ts_ratings[player1], ts_ratings[player2], drawn=True)
        ts_ratings[player1] = new_rating1
        ts_ratings[player2] = new_rating2
    ratings = [{"player": r[0], "rating": r[1].mu, "variance": r[1].sigma} for r in ts_ratings.items()]
    return ratings

def get_player_rating(game_sets, ranking_to_run="elo", evaluation_level="sets"):
    if ranking_to_run == "elo":
        simple_game_sets, id_to_player_name, player_to_id = process_game_sets_to_simple_format(game_sets, evaluation_level)
        ranking = run_elo(simple_game_sets)
    elif ranking_to_run == "trueskill":
        simple_game_sets, id_to_player_name, player_to_id = process_game_sets_to_simple_format(game_sets, evaluation_level)
        ranking = run_trueskill(simple_game_sets)
    elif ranking_to_run == "bradleyterry":
        game_sets_filtered = filter_game_sets(game_sets, threshold_sets=20, threshold_games=None)
        simple_game_sets_filtered, id_to_player_name, player_to_id = process_game_sets_to_simple_format(game_sets_filtered, evaluation_level)
        ranking = run_bradley_terry(simple_game_sets_filtered)
    return ranking, id_to_player_name, player_to_id


def find_incomplete_players(game_sets, sets_threshold=None, games_threshold=None):
    # Dictionaries to track sets and games count per player
    sets_count = defaultdict(int)
    games_count = defaultdict(int)

    # Count sets and games for each player
    for game_set in game_sets:
        player_1, player_2 = game_set["id_1"], game_set["id_2"]
        sets_count[player_1] += 1
        sets_count[player_2] += 1
        games_count[player_1] += game_set["score_1"] + game_set["score_2"]
        games_count[player_2] += game_set["score_1"] + game_set["score_2"]

    # Identify players who do not meet the thresholds
    incomplete_players = set()
    for player_id in sets_count.keys():
        if (sets_threshold is not None and sets_count[player_id] < sets_threshold) or \
                (games_threshold is not None and games_count[player_id] < games_threshold):
            incomplete_players.add(player_id)

    return incomplete_players


def filter_out_players_games(game_sets, player_ids):
    # Filter game sets to exclude any set where one of the players is in player_ids
    return [game_set for game_set in game_sets if
            game_set["id_1"] not in player_ids and game_set["id_2"] not in player_ids]


def filter_game_sets(game_sets, threshold_sets=None, threshold_games=None):
    # Get players who haven't met the threshold for sets and games
    incomplete_players = find_incomplete_players(game_sets, threshold_sets, threshold_games)

    # Filter out game sets that include any of these incomplete players
    return filter_out_players_games(game_sets, incomplete_players)


# Each game set looks like this:
# {
#   "player_1": "LG | Tweek",
#   "id_1": 12394650,
#   "score_1": 3,
#   "player_2": "Riddles",
#   "id_2": 12277894,
#   "score_2": 1,
#   "winner_id": 12394650
# }
# and set_list is just a list of these game set dictionaries.

# make function that takes in a set of games and gets a set of player ids that have not completed sets_threshold sets and games_threshold games
# if sets_threshold is None, then ignore that threshold requirement, if games_threshold is None then ignore that threshold requirement.
# in each game set, the score_1 + score_2 is the total number of GAMES played in that set.  One game set dict corresponds to one SET played.
# Make it very fast and memory efficient but also simple.

# make function that takes a list of player ids and list of game sets and returns only the game sets in which those players do not play (as id_1 or id_2)

# make a function called filter_game_sets that takes in the game sets list and filters all game sets containing players who have not yet played threshold_sets and threshold_games









