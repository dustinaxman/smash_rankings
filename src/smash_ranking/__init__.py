import trueskill as ts
from collections import defaultdict
import networkx as nx
import choix
import numpy as np
import logging
from datetime import datetime
from glicko2 import Player as Glicko2Player
import math
from scipy.stats import norm
from time import time
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import cg
from scipy.sparse import coo_matrix
from functools import reduce
from fractions import Fraction
import os
from src.utils.constants import LOG_FOLDER_PATH

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lcm(a, b):
    return a * b // math.gcd(a, b)

def get_scaling_factor_integer(list_of_floats_to_normalize):
    # Convert all fractional parts to fractions and extract denominators
    denominators = [
        Fraction(n).limit_denominator().denominator for n in list_of_floats_to_normalize
    ]

    # Find the LCM of all denominators
    scaling_factor = reduce(lcm, denominators)

    return scaling_factor


def process_game_sets_to_simple_format(game_sets, evaluation_level, tournament_tier_weights=None):
    logger.info("Processing games to simple form (process_game_sets_to_simple_format)")
    simple_game_sets = []
    id_to_player_name = dict()
    player_to_id = dict()
    initial_date = datetime(1500, 7, 20)
    last_updated_date_for_id = defaultdict(lambda: initial_date)
    tournament_tier_weights_base = defaultdict(lambda: 1.0)
    if tournament_tier_weights is not None:
        tournament_tier_weights_base.update(**tournament_tier_weights)
    print(tournament_tier_weights_base)
    # if tournament_tier_weights is not None:
    #     used_tiers = list(set([game_set["tier"] for game_set in game_sets]))
    #     scaling_factor = get_scaling_factor_integer([tournament_tier_weights[tier] for tier in used_tiers])
    #     normalized_scaling_map = {k: round(scaling_factor * tournament_tier_weights[k]) for k in used_tiers}
    #     print(normalized_scaling_map)

    for game_set in sorted(game_sets, key=lambda g: datetime.fromisoformat(g["date"])):
        player_1_name = str(game_set["player_1"])
        player_2_name = str(game_set["player_2"])
        player_1_id = game_set["id_1"]
        player_2_id = game_set["id_2"]
        # if player_1_id == "e2974569" and player_2_id == "e2974569":
        #     print(game_set)
        #     print("BIG DOG")
        #     exit(1)
        # if "Zomba" in [player_1_name, player_2_name]:
        #     print(game_set["score_1"], game_set["score_2"], player_1_name, player_2_name, game_set["winner_id"], player_1_id, player_2_id)
        if player_1_id is None or player_2_id is None or player_1_id == "" or player_2_id == "":
            continue
        if game_set["score_1"] is None or game_set["score_2"] is None:
            continue
        if (game_set["score_1"] == 0 and game_set["score_2"] == 0) or game_set["score_1"] < 0 or game_set["score_2"] < 0:
            continue
        # if "Moist | Light" in [player_1_name, player_2_name]:
        #     print(game_set)
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
        # if player_1_name in player_to_id:
        #     if player_1_id != "b2fa1c21": # Light has 2 accounts AND there is another player with the tag "Light" https://www.start.gg/user/b2fa1c21/details
        #         player_1_id = player_to_id[player_1_name]
        # if player_2_name in player_to_id:
        #     if player_2_id != "b2fa1c21": # Light has 2 accounts AND there is another player with the tag "Light" https://www.start.gg/user/b2fa1c21/details
        #         player_2_id = player_to_id[player_2_name]
        if player_1_id == "1f378ab2":
            player_1_id = "e2974569"
        if player_2_id == "1f378ab2":
            player_2_id = "e2974569"
        if player_1_id == "263c6038":
            player_1_id = "b5230de8"
        if player_2_id == "263c6038":
            player_2_id = "b5230de8"
        if player_1_id == "205aeef6":
            player_1_id = "b5230de8"
        if player_2_id == "205aeef6":
            player_2_id = "b5230de8"
        #
        # if "Sparg" in player_1_name:
        #     if player_1_id != "b5230de8":
        #         print(player_1_name, player_1_id)
        # if "Sparg" in player_2_name:
        #     if player_2_id != "b5230de8":
        #         print(player_2_name, player_2_id)

        current_date = datetime.fromisoformat(game_set["date"])
        if current_date > last_updated_date_for_id[player_1_id]:
            id_to_player_name[player_1_id] = player_1_name
            last_updated_date_for_id[player_1_id] = current_date
        if current_date > last_updated_date_for_id[player_2_id]:
            id_to_player_name[player_2_id] = player_2_name
            last_updated_date_for_id[player_2_id] = current_date
        player_to_id[player_1_name] = player_1_id
        player_to_id[player_2_name] = player_2_id
        #simple_game_sets.extend([[player_1_id, player_2_id, score1, score2]]*normalized_scaling_map[game_set["tier"]])
        simple_game_sets.append([player_1_id, player_2_id, score1, score2, tournament_tier_weights_base[game_set["tier"]]])
        #if player_1_id == "e2974569" and player_2_id == "e2974569":
        #     print(game_set)
        #     print("SMALL DOG")
        #     exit(1)
    logger.info("FINISHED process_game_sets_to_simple_format")
    logger.info(len(simple_game_sets))
    print(len(simple_game_sets))
    return simple_game_sets, id_to_player_name, player_to_id


#TODO: # #Glicko/Glicko-2???
#TODO:  #Bayesian Elo
def run_bradley_terry(simple_game_sets, max_iter=1000, tol=1e-4, alpha=0.1):
    """
    Computes Bradley-Terry ratings from game data.

    Parameters:
    - simple_game_sets: list of tuples (player1, player2, score1, score2)
        Each tuple represents a match between player1 and player2 with their respective scores.
    - max_iter: int
        Maximum number of iterations for the optimizer.
    - tol: float
        Tolerance for convergence.
    - alpha: float
        Regularization parameter to prevent overfitting and help convergence.

    Returns:
    - ratings: List of dictionaries with 'player', 'rating', and 'uncertainty' keys.
    """
    start = time()
    comparisons_counts = defaultdict(int)
    G = nx.DiGraph()
    for player1, player2, score1, score2 in simple_game_sets:
        score1 = int(score1)
        score2 = int(score2)

        # Skip matches with no score
        if score1 == 0 and score2 == 0:
            continue

        # Add edges for wins
        if score1 > 0:
            comparisons_counts[(player1, player2)] += score1
            G.add_edge(player1, player2)
        if score2 > 0:
            comparisons_counts[(player2, player1)] += score2
            G.add_edge(player2, player1)
    # Check if graph is empty
    if G.number_of_nodes() == 0:
        logger.error("No valid games provided.")
        raise ValueError("No valid games provided.")

    # Step 2: Find strongly connected components
    sccs = list(nx.strongly_connected_components(G))

    # Sort components by size
    sccs.sort(key=lambda scc: len(scc), reverse=True)
    largest_scc = sccs[0]

    # Log the size of the largest SCC
    logger.info("Largest strongly connected component size: {}".format(len(largest_scc)))

    # Check if largest SCC is too small
    if len(largest_scc) < 2:
        logger.error("Largest strongly connected component is too small to compute ratings.")
        raise ValueError("Largest strongly connected component is too small to compute ratings.")

    # Step 3: Filter comparisons to keep only those within the largest SCC
    comparisons_counts_filtered = {
        (p1, p2): count
        for (p1, p2), count in comparisons_counts.items()
        if p1 in largest_scc and p2 in largest_scc
    }

    # Step 4: Map players to indices within the largest SCC
    players = list(largest_scc)
    player_idx = {p: i for i, p in enumerate(players)}
    n_players = len(players)

    # Step 5: Prepare data for choix.mm_pairwise
    comparisons_numeric = []
    counts = []

    for (p1, p2), count in comparisons_counts_filtered.items():
        comparisons_numeric.append((player_idx[p1], player_idx[p2]))
        counts.append(count)

    # Expand comparisons according to counts
    expanded_comparisons = []
    for (i, j), count in zip(comparisons_numeric, counts):
        expanded_comparisons.extend([(i, j)] * count)

    # Step 6: Run Bradley-Terry model using mm_pairwise
    initial_params = np.zeros(n_players)  # Start with zero log-abilities
    try:
        bt_ratings = choix.mm_pairwise(
            n_items=n_players,
            data=expanded_comparisons,
            alpha=alpha,
            initial_params=initial_params,
            max_iter=max_iter,
            tol=tol,
        )
    except RuntimeError as e:
        logger.error("MM algorithm did not converge: {}".format(e))
        raise
    # Normalize ratings (optional)
    bt_ratings -= np.mean(bt_ratings)  # Center the ratings

    # Identify top 100 players based on ratings
    top_100_indices = np.argsort(bt_ratings)[-100:]  # Indices of the top 100 players

    # Compute the Hessian matrix efficiently for the top 100 players only
    i_array = np.array([i for (i, j) in comparisons_numeric])
    j_array = np.array([j for (i, j) in comparisons_numeric])
    count_array = np.array(counts)

    delta_array = bt_ratings[i_array] - bt_ratings[j_array]
    exp_delta = np.exp(delta_array)
    p = exp_delta / (1 + exp_delta)
    w = count_array * p * (1 - p)

    data = np.concatenate([w, w, -w, -w])
    row = np.concatenate([i_array, j_array, i_array, j_array])
    col = np.concatenate([i_array, j_array, j_array, i_array])

    H_sparse = coo_matrix((data, (row, col)), shape=(n_players, n_players))
    H_sparse = H_sparse.tocsr()
    H_sparse.setdiag(H_sparse.diagonal() + alpha)

    # Compute variances only for the top 100 players
    variances = np.full(n_players, None)  # Initialize with None for all
    for i in top_100_indices:
        e_i = np.zeros(n_players)
        e_i[i] = 1.0

        x_i, info = cg(H_sparse, e_i, x0=None, rtol=1e-2, maxiter=10)
        variances[i] = x_i[i]  # Diagonal element for the inverse Hessian

    standard_errors = np.sqrt([v if v is not None else 0 for v in variances])
    z = norm.ppf(1 - 0.025)  # Approximately 1.96 for 95% confidence
    uncertainty = z * standard_errors
    # Build the ratings list with None for players not in the top 100
    ratings = []
    for idx, (p, r, u) in enumerate(zip(players, bt_ratings, uncertainty)):
        ratings.append({
            "player": p,
            "rating": r,
            "uncertainty": u if idx in top_100_indices else None
        })

    return ratings


def run_simple_elo(simple_game_sets):
    logger.info("START run_simple_elo")
    elo_ratings = defaultdict(lambda: 1200)  # Default initial rating of 1200
    games_played = defaultdict(int)  # Track total games played per player
    simple_game_sets_len = len(simple_game_sets)
    logger.info(simple_game_sets_len)
    #looped_unrolled_matchups = [matchup for s in [simple_game_sets for epoch in range(50)] for matchup in s]
    #simple_game_sets_len*100
    # 3 million chosen for rough number of total games in a FIDE period that is stable.  Rounded to nearest epoch
    for matchup in simple_game_sets:
        player1, player2, score1, score2, weight = matchup
        total_games = score1 + score2
        if total_games == 0:
            continue
        games_played[player1] += total_games
        games_played[player2] += total_games

        # # Determine if players are provisional based on games played
        # is_provisional1 = games_played[player1] < 30
        # is_provisional2 = games_played[player2] < 30

        # # Skip Elo adjustment for established players facing provisional opponents
        # if not is_provisional1 and is_provisional2:
        #     continue
        # if not is_provisional2 and is_provisional1:
        #     continue

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
        # if matchup_idx == 0 and matchup_count >= simple_game_sets_len and max(elo_ratings.values()) > 2800:
        #     break
    logger.info("FINISHED run_simple_elo")
    # Prepare results in desired format
    # rating*((1 / (1 + np.exp(((uncertainty)-21)/200))) + 0.5) if uncertainty > 60 else "Honorable Mention"
    ratings = [{"player": player, "rating": rating, "uncertainty": 2000/games_played[player]} for player, rating in elo_ratings.items()]
    return ratings


def run_elo(simple_game_sets):
    logger.info("START run_elo")
    elo_ratings = defaultdict(lambda: 1200)  # Default initial rating of 1200
    games_played = defaultdict(int)  # Track total games played per player
    simple_game_sets_len = len(simple_game_sets)
    logger.info(simple_game_sets_len)
    #looped_unrolled_matchups = [matchup for s in [simple_game_sets for epoch in range(50)] for matchup in s]
    #simple_game_sets_len*100
    # for matchup_idx in range(simple_game_sets_len):
    #     matchup = simple_game_sets[matchup_idx]
    #     player1, player2, score1, score2 = matchup
    #     if player1 == "e2974569" and player2 == "e2974569":
    #         print("STOP THE DOG")
    #         print(score1, score2)
    #         exit(1)
    # 3 million chosen for rough number of total games in a FIDE period that is stable.  Rounded to nearest epoch
    player_update_tracker = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: [0, 0])))
    total_games_to_run = max(int(5000000 / simple_game_sets_len), 1) * simple_game_sets_len
    print("TOTAL GAMES TO RUN", total_games_to_run)
    for matchup_count in range(total_games_to_run):
        matchup_idx = matchup_count % simple_game_sets_len
        matchup = simple_game_sets[matchup_idx]
        player1, player2, score1, score2, weight = matchup
        # TODO, use the weight here in the most ideal way possible to make
        total_games = score1 + score2
        if total_games == 0:
            continue
        if matchup_count < simple_game_sets_len:
            games_played[player1] += total_games*weight*.75
            games_played[player2] += total_games*weight*.75

        # # Determine if players are provisional based on games played
        # is_provisional1 = games_played[player1] < 30
        # is_provisional2 = games_played[player2] < 30

        # # Skip Elo adjustment for established players facing provisional opponents
        # if not is_provisional1 and is_provisional2:
        #     continue
        # if not is_provisional2 and is_provisional1:
        #     continue

        # Set K-factor based on experience and rating
        def get_k_factor(player):
            if games_played[player] < 30:  # Provisional player
                return 10
            elif elo_ratings[player] >= 2400:  # Top player
                return 10
            else:  # Established player
                return 10

        k_factor1 = get_k_factor(player1)
        k_factor2 = get_k_factor(player2)

        # Calculate expected scores for both players
        expected_score1 = 1 / (1 + 10 ** ((elo_ratings[player2] - elo_ratings[player1]) / 400))
        expected_score2 = 1 - expected_score1

        # Calculate actual scores as proportions
        actual_score1 = score1 / total_games
        actual_score2 = score2 / total_games

        # Update ratings based on K-factors and actual vs expected scores
        p1_update = weight * k_factor1 * (actual_score1 - expected_score1)
        p2_update = weight * k_factor2 * (actual_score2 - expected_score2)
        elo_ratings[player1] += p1_update
        elo_ratings[player2] += p2_update

        if score1 > score2:
            if matchup_count < simple_game_sets_len:
                player_update_tracker[player1][player2]["win"][0] += 1
                player_update_tracker[player2][player1]["loss"][0] += 1
            player_update_tracker[player1][player2]["win"][1] += p1_update
            player_update_tracker[player2][player1]["loss"][1] += p2_update
        else:
            if matchup_count < simple_game_sets_len:
                player_update_tracker[player1][player2]["loss"][0] += 1
                player_update_tracker[player2][player1]["win"][0] += 1
            player_update_tracker[player1][player2]["loss"][1] += p1_update
            player_update_tracker[player2][player1]["win"][1] += p2_update
        # all_win_loss_record[player1].append((player2, 1 if matchup_count < simple_game_sets_len else 0, "win" if score1 > score2 else "loss", p1_update))
        # all_win_loss_record[player2].append((player1, 1 if matchup_count < simple_game_sets_len else 0, "win" if score1 < score2 else "loss", p2_update))
        # if matchup_idx == 0 and matchup_count >= simple_game_sets_len and max(elo_ratings.values()) > 2800:
        #     break
    logger.info("FINISHED run_elo")
    print(len(elo_ratings))
    # Prepare results in desired format # - 2000/games_played[player]
    ratings = [{"player": player, "rating": rating, "uncertainty": 8000/games_played[player]} for player, rating in elo_ratings.items()]
    return ratings, player_update_tracker


def run_trueskill(simple_game_sets):
    logger.info("START run_trueskill")
    env = ts.TrueSkill()
    ts_ratings = defaultdict(lambda: env.create_rating())
    for matchup in simple_game_sets:
        player1, player2, score1, score2, weight = matchup
        total_games = score1 + score2
        if total_games == 0:
            continue

        # Unroll multiple games into individual 1-0 or 0-1 results
        game_sequence = []
        game_sequence.extend([1] * int(score1))  # Add player1's wins
        game_sequence.extend([0] * int(score2))  # Add player2's wins
        # Process each individual game
        for game_result in game_sequence:
            if game_result == 1:  # Player 1 wins
                new_rating1, new_rating2 = env.rate_1vs1(ts_ratings[player1], ts_ratings[player2])
            else:  # Player 2 wins
                new_rating2, new_rating1 = env.rate_1vs1(ts_ratings[player2], ts_ratings[player1])
            ts_ratings[player1] = new_rating1
            ts_ratings[player2] = new_rating2
    logger.info("FINISHED run_trueskill")
    ratings = [{"player": r[0], "rating": r[1].mu -r[1].sigma, "uncertainty": 1.96 * r[1].sigma} for r in ts_ratings.items()]
    return ratings

# def _rate_1vs1_custom(rating1, rating2, env, drawn=False):
#     """
#     Computes the rating updates for a single 1vs1 game without constructing
#     the factor graph, ensuring exact results as `env.rate_1vs1`.
#
#     :param rating1: Rating of the first player.
#     :param rating2: Rating of the second player.
#     :param env: The TrueSkill environment.
#     :param drawn: Boolean indicating if the game was a draw.
#     :return: Updated ratings for rating1 and rating2.
#     """
#     # Initial means and standard deviations
#     mu1, sigma1 = rating1.mu, rating1.sigma
#     mu2, sigma2 = rating2.mu, rating2.sigma
#
#     # Precompute the performance variance
#     beta_squared = env.beta ** 2
#     sigma1_squared = sigma1 ** 2
#     sigma2_squared = sigma2 ** 2
#     pi_squared = math.pi ** 2
#
#     # Performance difference variance
#     c = math.sqrt(2 * beta_squared + sigma1_squared + sigma2_squared)
#
#     # The mean difference divided by the performance difference variance
#     t = (mu1 - mu2) / c
#
#     # Calculate the draw margin
#     draw_margin = env.draw_margin(2)
#
#     # Adjust t and draw_margin for the c scaling
#     adj_draw_margin = draw_margin / c
#
#     if drawn:
#         v = env.v_draw(t, adj_draw_margin)
#         w = env.w_draw(t, adj_draw_margin)
#     else:
#         v = env.v_win(t, adj_draw_margin)
#         w = env.w_win(t, adj_draw_margin)
#
#     # Update means
#     delta_mu1 = (sigma1_squared / c) * v
#     delta_mu2 = -(sigma2_squared / c) * v
#     mu1 += delta_mu1
#     mu2 += delta_mu2
#
#     # Update standard deviations
#     sigma1 *= math.sqrt(max(1 - (sigma1_squared / c ** 2) * w, 1e-6))
#     sigma2 *= math.sqrt(max(1 - (sigma2_squared / c ** 2) * w, 1e-6))
#
#     # Return updated ratings
#     new_rating1 = ts.Rating(mu=mu1, sigma=sigma1)
#     new_rating2 = ts.Rating(mu=mu2, sigma=sigma2)
#     return new_rating1, new_rating2

# Add the draw_margin method to the TrueSkill class
def draw_margin(self, size):
    return ts.calc_draw_margin(self.draw_probability, size, self)

# Monkey-patch the method
ts.TrueSkill.draw_margin = draw_margin

def get_player_rating(game_sets, ranking_to_run="elo", evaluation_level="sets", tournament_tier_weights=None):
    top_win_loss_record = None
    if ranking_to_run == "elo":
        simple_game_sets, id_to_player_name, player_to_id = process_game_sets_to_simple_format(game_sets, evaluation_level, tournament_tier_weights=tournament_tier_weights)
        simple_game_sets_len = len(simple_game_sets)
        for matchup_idx in range(simple_game_sets_len):
            matchup = simple_game_sets[matchup_idx]
            player1, player2, score1, score2, weight = matchup
            # if player1 == "e2974569" and player2 == "e2974569":
            #     print("STOP THE CAT")
            #     print(score1, score2)
            #     exit(1)
        ranking, top_win_loss_record = run_elo(simple_game_sets)
    elif ranking_to_run == "trueskill":
        start = time()
        simple_game_sets, id_to_player_name, player_to_id = process_game_sets_to_simple_format(game_sets, evaluation_level, tournament_tier_weights=tournament_tier_weights)
        print(f"finished process_game_sets_to_simple_format", time()-start)
        ranking = run_trueskill(simple_game_sets)
    elif ranking_to_run == "bradleyterry":
        game_sets_filtered = filter_game_sets(game_sets, threshold_sets=None, threshold_games=None)
        simple_game_sets_filtered, id_to_player_name, player_to_id = process_game_sets_to_simple_format(game_sets_filtered, evaluation_level, tournament_tier_weights=tournament_tier_weights)
        ranking = run_bradley_terry(simple_game_sets_filtered)
    elif ranking_to_run == "glicko2":
        simple_game_sets, id_to_player_name, player_to_id = process_game_sets_to_simple_format(game_sets,
                                                                                               evaluation_level, tournament_tier_weights=tournament_tier_weights)
        ranking = run_glicko2(simple_game_sets)
    elif ranking_to_run == "simpleelo":
        simple_game_sets, id_to_player_name, player_to_id = process_game_sets_to_simple_format(game_sets,
                                                                                               evaluation_level, tournament_tier_weights=tournament_tier_weights)
        ranking = run_simple_elo(simple_game_sets)
    elif ranking_to_run == "bayesianelo":
        simple_game_sets, id_to_player_name, player_to_id = process_game_sets_to_simple_format(game_sets,
                                                                                               evaluation_level, tournament_tier_weights=tournament_tier_weights)
        ranking = bayesian_elo(simple_game_sets)
    return ranking, id_to_player_name, player_to_id, top_win_loss_record


def find_incomplete_players(game_sets, sets_threshold=None, games_threshold=None):
    # Dictionaries to track sets and games count per player
    sets_count = defaultdict(int)
    games_count = defaultdict(int)

    # Count sets and games for each player
    for game_set in game_sets:
        player_1, player_2 = game_set["id_1"], game_set["id_2"]
        if game_set["score_1"] is None or game_set["score_2"] is None:
            continue
        if (game_set["score_1"] == 0 and game_set["score_2"] == 0) or game_set["score_1"] < 0 or game_set["score_2"] < 0:
            continue
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



def run_glicko2(simple_game_sets, initial_rating=1500, initial_rd=350, initial_volatility=0.06):
    """
    Computes Glicko-2 ratings based on match outcomes using the `glicko2` library.

    Parameters:
    - simple_game_sets: List of match results in the format [(player1, player2, score1, score2), ...]
    - initial_rating: Initial rating for new players
    - initial_rd: Initial rating deviation for new players
    - initial_volatility: Initial volatility for new players

    Returns:
    - List of player ratings with rating, rating deviation, and volatility.
    """
    # Initialize a dictionary to store Glicko2Player instances
    glicko_ratings = defaultdict(lambda: Glicko2Player(initial_rating, initial_rd, initial_volatility))

    # Process each match outcome
    for matchup in simple_game_sets:
        player1, player2, score1, score2, weight = matchup
        total_games = score1 + score2
        if total_games == 0:
            continue  # Skip if there are no games played

        # Determine the match outcome (win, loss, or draw)
        if score1 > score2:
            result1, result2 = 1, 0  # player1 wins
        elif score2 > score1:
            result1, result2 = 0, 1  # player2 wins
        else:
            result1, result2 = 0.5, 0.5  # draw

        # Get Glicko2Player instances for both players
        player1_obj = glicko_ratings[player1]
        player2_obj = glicko_ratings[player2]

        # Update ratings for both players based on match outcome
        player1_obj.update_player([player2_obj.rating], [player2_obj.rd], [result1])
        player2_obj.update_player([player1_obj.rating], [player1_obj.rd], [result2])

    # Prepare the output in a structured format
    ratings = [
        {
            "player": player,
            "rating": player_obj.rating,
            "uncertainty": 1.96 * player_obj.rd
        }
        for player, player_obj in glicko_ratings.items()
    ]
    return ratings

def bayesian_elo(matches, initial_rating=1200, k_factor=10, variance=200):
    """
    Computes Bayesian Elo ratings for players based on a list of matches.

    Args:
    - matches (list of lists): Each entry is a list [player_1_id, player_2_id, score1, score2]
      where `score1` and `score2` are the respective scores for player_1 and player_2.
      `score1` > `score2` means player_1 wins, and vice versa.
    - initial_rating (int, optional): The initial rating for each player. Default is 1500.
    - k_factor (float, optional): The learning rate or adjustment factor for the Elo update.
    - variance (float, optional): Initial variance in the ratings, reflecting uncertainty.

    Returns:
    - list of dicts: Each dict contains "player", "rating", and "variance" for each player.

    """

    # Player rating and variance initialization
    player_ratings = defaultdict(lambda: {"rating": initial_rating, "variance": variance})

    def expected_score(rating1, rating2, variance1, variance2):
        # Expectation based on normal distribution assumption for Bayesian Elo
        return 1 / (1 + math.exp((rating2 - rating1) / math.sqrt(variance1 + variance2)))

    def update_ratings(player1, player2, score1, score2):
        # Retrieve current ratings and variances
        r1, v1 = player_ratings[player1]["rating"], player_ratings[player1]["variance"]
        r2, v2 = player_ratings[player2]["rating"], player_ratings[player2]["variance"]

        # Compute expected scores
        E1 = expected_score(r1, r2, v1, v2)
        E2 = 1 - E1

        # Determine actual score outcome
        S1 = 1 if score1 > score2 else 0.5 if score1 == score2 else 0
        S2 = 1 - S1

        # Update ratings
        player_ratings[player1]["rating"] += k_factor * (S1 - E1)
        player_ratings[player2]["rating"] += k_factor * (S2 - E2)

        # Update variances with Bayesian approach to adapt to more consistent performance
        player_ratings[player1]["variance"] = max(variance / 2, v1 * (1 - E1))
        player_ratings[player2]["variance"] = max(variance / 2, v2 * (1 - E2))

    # Process each match
    for match in matches:
        player1, player2, score1, score2 = match
        update_ratings(player1, player2, score1, score2)

    # Compile the results
    ratings = [
        {"player": player, "rating": info["rating"], "uncertainty": 1.96 * math.sqrt(info["variance"])}
        for player, info in player_ratings.items()
    ]
    return ratings

# Each game set looks like this:
# {
#   "date": <datetime object for set>
#   "player_1": "LG | Tweek",
#   "id_1": 12394650,
#   "score_1": 3,
#   "player_2": "Riddles",
#   "id_2": 12277894,
#   "score_2": 1,
#   "winner_id": 12394650
# }
# and set_list is just a list of these game set dictionaries.









