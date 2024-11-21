from collections import defaultdict
import random
import re
import copy
import time
import json
from pathlib import Path
import pandas as pd
import datetime
import logging
# import multiprocessing as mp
import torch.multiprocessing as mp
# try:
#      mp.set_start_method('spawn')
# except RuntimeError:
#     pass
from tqdm import tqdm
import pysmashgg
from torch import nn
import numpy as np
import torch
import boto3
import uuid
import hashlib
from scipy import special
import math
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('SmashRankingData')
s3 = boto3.resource('s3')
s3_client = boto3.client('s3')


logging.basicConfig(level=logging.INFO,
                    handlers=[logging.FileHandler(Path.home() / 'LOG.txt'), logging.StreamHandler()])

NUM_API_RETRIES = 5
K = 30
INITIAL_ELO = 1000
RETRY_COUNT = 3
ALL_TOURNAMENTS_GAMES_FILE = Path.home() / 'game_dict.json'
ALL_TOURNAMENTS_DATES_FILE = Path.home() / 'tournament_to_date_dict.json'


def nCr(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


def binom_integ(n, k, n_new, k_new):
    p_0 = (0.0 ** (k + k_new + 1)) * special.hyp2f1((k + k_new) + 1, (k + k_new) - (n + n_new), (k + k_new) + 2,
                                                    0.0) / ((k + k_new) + 1)
    p_1 = (1.0 ** (k + k_new + 1)) * special.hyp2f1((k + k_new) + 1, (k + k_new) - (n + n_new), (k + k_new) + 2,
                                                    1.0) / ((k + k_new) + 1)
    return nCr(n, k) * nCr(n_new, k_new) * (p_1 - p_0)


def prob_success_given_prev_trials(n, k):
    return binom_integ(n, k, 1, 1) / (binom_integ(n, k, 1, 1) + binom_integ(n, k, 1, 0))


def num_winning_matchups(list_of_matchups):
    return sum([m[0] >= m[1] for m in list_of_matchups])


def format_cells(c):
    if isinstance(c, float) and np.isnan(c):
        return "0:0"
    else:
        return "{}:{}".format(c[0], c[1])


def get_matchup_table(start_date=None, end_date=None, player_list=None, refresh_artifacts=False, resolution='sets'):
    start_date = datetime.datetime.strptime(start_date, '%m/%d/%Y')
    end_date = datetime.datetime.strptime(end_date, '%m/%d/%Y')
    tournament_to_date_dict = load_json(ALL_TOURNAMENTS_DATES_FILE)
    game_dict = load_json(ALL_TOURNAMENTS_GAMES_FILE)
    selected_tournament_urls = get_tournaments_from_date_range(tournament_to_date_dict, start_date=start_date,
                                                               end_date=end_date)
    logging.info("Selected the following tournaments from date range {} to {}:".format(start_date, end_date))
    logging.info("\n".join(selected_tournament_urls))
    all_games = get_game_list_from_list_of_tournaments(game_dict, selected_tournament_urls)
    if resolution == "sets":
        all_games = convert_game_score_to_winlose_set(all_games)
    matchups, player_to_idx = get_matchups(all_games, player_list)
    matchup_table = defaultdict(lambda: defaultdict(list))
    for matchup in matchups:
        m1, m2, s1, s2 = matchup
        matchup_table[player_list[m1]][player_list[m2]] = [s1, s2]
        matchup_table[player_list[m2]][player_list[m1]] = [s2, s1]
    sorted_player_list = [p for p, _ in sorted(matchup_table.items(), key=lambda a: num_winning_matchups(a[1].values()),
                                               reverse=True)]
    df = pd.DataFrame(matchup_table).T
    sorted_df = df[sorted_player_list].reindex(sorted_player_list)
    formatted_df = sorted_df.applymap(format_cells)
    return formatted_df


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def get_recent_artifacts():
    tournament_to_date_dict_file = Path().home() / 'tournament_to_date_dict.json'
    game_dict_file = Path().home() / 'game_dict.json'
    if tournament_to_date_dict_file.exists():
        tournament_to_date_dict_file.unlink()
    if game_dict_file.exists():
        game_dict_file.unlink()
    response = table.get_item(
        Key={
            'DataInfo': 'Newest',
        }
    )
    tournament_to_date_dict_s3uri = response['Item']['tournament_to_date_dict_s3uri']
    game_dict_s3uri = response['Item']['game_dict_s3uri']
    s3.Bucket('smash-ranking').download_file(tournament_to_date_dict_s3uri, str(tournament_to_date_dict_file))
    s3.Bucket('smash-ranking').download_file(game_dict_s3uri, str(game_dict_file))


def update_s3_ddb_with_new_artifacts():
    datestamp = str(datetime.datetime.now()).replace(" ", "-")
    checksum = str(uuid.uuid4())
    tournament_to_date_dict_s3uri = f"data/{datestamp}/tournament_to_date_dict_{checksum}.json"
    game_dict_s3uri = f"data/{datestamp}/game_dict_{checksum}.json"
    s3.Bucket('smash-ranking').upload_file(str(Path().home() / 'tournament_to_date_dict.json'),
                                           tournament_to_date_dict_s3uri)
    s3.Bucket('smash-ranking').upload_file(str(Path().home() / 'game_dict.json'), game_dict_s3uri)
    table.delete_item(Key={'DataInfo': 'Newest'})
    table.put_item(
        Item={
            "DataInfo": "Newest",
            "date": datestamp,
            "tournament_to_date_dict_s3uri": tournament_to_date_dict_s3uri,
            "game_dict_s3uri": game_dict_s3uri
        }
    )


def update_tournament_cache_and_upload(new_tournaments):
    get_recent_artifacts()
    game_dict = update_tournament_cache(new_tournaments)
    update_s3_ddb_with_new_artifacts()
    return game_dict


def update_tournament_cache(new_tournaments):
    tournament_to_date_dict = create_tournament_to_date_dict(new_tournaments)
    write_json(tournament_to_date_dict, ALL_TOURNAMENTS_DATES_FILE, append=True)
    game_dict = load_tournament_data(new_tournaments)
    write_json(game_dict, ALL_TOURNAMENTS_GAMES_FILE, append=True)
    return game_dict


def convert_game_score_to_winlose_set(sets_list):
    normalized_sets_list = []
    for match in sets_list:
        if match[1] > match[3]:
            normalized_sets_list.append([match[0], 1, match[2], 0])
        elif match[1] < match[3]:
            normalized_sets_list.append([match[0], 0, match[2], 1])
        else:
            normalized_sets_list.append([match[0], 1, match[2], 1])
    return normalized_sets_list


def convert_score(score):
    if score == 'W':
        return 1
    elif score == 'L':
        return 0
    elif score == 'DQ':
        pass
    elif score == '-':
        return 0
    elif score == '':
        pass
    elif score < 0:
        pass
    else:
        return int(score)


def convert_set_to_game_form(set_dict):
    player1 = set_dict["entrant1Players"][0]["playerTag"]
    score1 = convert_score(set_dict["entrant1Score"])
    player2 = set_dict["entrant2Players"][0]["playerTag"]
    score2 = convert_score(set_dict["entrant2Score"])
    return [player1, score1, player2, score2]


def api_set_grabber_wrapper(tourn_name, bracket, i):
    retry_idx = 0
    sets_list = []
    while retry_idx < NUM_API_RETRIES and len(sets_list) == 0:
        if retry_idx > 0:
            time.sleep(30)
            logging.info(f"RETRYING {retry_idx}")
        try:
            sets_list = SMASH.tournament_show_sets(tourn_name, bracket, i)
        except TypeError as e:
            logging.info("Failed call: {}".format(str(e)))
        retry_idx += 1
    if len(sets_list) == 0:
        logging.info("All retries failed to return non-empty set list")
        return
    else:
        return sets_list


def get_games_from_tournament_url(url):
    tourn_name = url.split("/")[4]
    bracket = url.split("/")[6]
    all_sets = []
    i = 0
    while True:
        logging.info(str(i))
        sets_list = api_set_grabber_wrapper(tourn_name, bracket, i)
        if sets_list is None or len(sets_list) == 0:
            break
        all_sets.extend(sets_list)
        time.sleep(1.2)
        i += 1
    converted_sets = []
    for s in all_sets:
        try:
            game = convert_set_to_game_form(s)
            if game[1] is not None and game[3] is not None:  # check if any were dropped by convert score (pass)
                converted_sets.append(game)
        except:
            logging.warning("BAD SET in {} :  {}".format(url, str(s)))
    return converted_sets


def load_tournament_data(tournament_url_list):
    game_dict = {}
    for tournament_url in tournament_url_list:
        logging.info(tournament_url)
        game_dict[tournament_url] = get_games_from_tournament_url(tournament_url)
        # for page_idx in range(1, num_pages+1):
        #   print(tournament_url+'?page=' + str(page_idx))
        #   table = load_table_from_page(tournament_url+'?page=' + str(page_idx))
        #   game_list.extend(table)
        write_json(game_dict, ALL_TOURNAMENTS_GAMES_FILE, append=True)
    write_json(game_dict, Path.home() / 'tmp.json')
    return game_dict


def group_game_dict_to_games(game_dict):
    all_games = []
    for g in game_dict.values():
        all_games.extend(g)
    return all_games


def check_date_between(date, start_date, end_date):
    if start_date is not None:
        if date < start_date:
            return False
    if end_date is not None:
        if date > end_date:
            return False
    return True


def get_tournaments_from_date_range(tournament_to_date_dict, start_date=None, end_date=None):
    selected_tournament_urls = [tournament_url for tournament_url, date in tournament_to_date_dict.items() if
                                check_date_between(date, start_date, end_date)]
    return selected_tournament_urls


def get_game_list_from_list_of_tournaments(game_dict, selected_tournament_urls):
    selected_game_dict = {k: game_dict[k] for k in selected_tournament_urls}
    return group_game_dict_to_games(selected_game_dict)


def serialize_datetimes(dict_val):
    return {k: (v.strftime('%s') if isinstance(v, datetime.datetime) else v) for k, v in dict_val.items()}


def deserialize_datetimes(dict_val):
    # convert all to datetimes
    return {k: (datetime.datetime.fromtimestamp(int(v)) if isinstance(v, str) and v.isdigit() else v) for k, v in
            dict_val.items()}


def write_json(dict_to_write, filename, append=False):
    if Path(filename).exists() and append:
        existing_dict = load_json(filename)
    else:
        existing_dict = {}
    existing_dict.update(dict_to_write)
    with open(filename, 'w') as f:
        existing_dict = serialize_datetimes(existing_dict)
        json.dump(existing_dict, f)


def load_json(filename):
    with open(filename, 'r') as f:
        dict_val = json.load(f)
    dict_val = deserialize_datetimes(dict_val)
    return dict_val


def create_tournament_to_date_dict(tournament_url_list):
    tournament_to_date_dict = {}
    for url in tournament_url_list:
        tourn_name = url.split("/")[4]
        bracket = url.split("/")[6]
        if "evo-2019" == tourn_name:
            tournament_to_date_dict[url] = datetime.datetime.fromtimestamp(1564740000)
        elif "sp6-umeburasp6" == tourn_name:
            tournament_to_date_dict[url] = datetime.datetime.fromtimestamp(1571652000)
        else:
            tournament_info = SMASH.tournament_show_with_brackets(tourn_name, bracket)
            time.sleep(1.2)
            tournament_to_date_dict[url] = datetime.datetime.fromtimestamp(tournament_info["startTimestamp"])
    return tournament_to_date_dict


def game_list_unroll(game_list):
    new_game_list = []
    for game in game_list:
        try:
            for i1 in range(game[1]):
                new_game_list.append([game[0], 1, game[2], 0])
            for i2 in range(game[3]):
                new_game_list.append([game[0], 0, game[2], 1])
        except:
            logging.warning("Cant unroll: {}".format(str(game)))
    return new_game_list


def display_player_rating(player_to_rating_dict, top=None):
    player_to_rating_sorted = sorted(player_to_rating_dict.items(), key=lambda a: a[1], reverse=True)
    if top is not None:
        num_to_display = min(top, len(player_to_rating_sorted))
    else:
        num_to_display = len(player_to_rating_sorted)
    for i in range(num_to_display):
        player, elo = player_to_rating_sorted[i]
        print('{}: {}'.format(player, elo))
    print('')
    print('')


def iterate_through_game_list_update_elo(game_list, num_epochs=1):
    player_to_rating_dict = defaultdict(lambda: INITIAL_ELO)
    for i in range(num_epochs * len(game_list)):
        player_a, did_A_win, player_b, did_B_win = game_list[i % len(game_list)]
        rating_a = player_to_rating_dict[player_a]
        rating_b = player_to_rating_dict[player_b]
        tmp = 10 ** ((rating_b - rating_a) / 400)
        chance_of_A_winning = 1 / (1 + tmp)
        chance_of_B_winning = 1 / (1 + (1 / tmp))
        player_to_rating_dict[player_a], player_to_rating_dict[player_b] = rating_a + K * (
        did_A_win - chance_of_A_winning), rating_b + K * (did_B_win - chance_of_B_winning)
    return player_to_rating_dict


def filter_game_list_by_min_matches(game_list_unrolled, n=5):
    player_game_count = defaultdict(int)
    for game in game_list:
        player1, score1, player2, score2 = game
        player_game_count[player1] += 1
        player_game_count[player2] += 1
    allowed_player_set = {k for k, v in player_game_count.items() if v >= n}
    return [game for game in game_list if game[0] in allowed_player_set and game[2] in allowed_player_set]


def get_player_matchups(game_list, player):
    player_matchup = defaultdict(lambda: [0, 0])
    for game in game_list:
        p1, s1, p2, s2 = game
        if player == p1:
            player_matchup[p2] = [player_matchup[p2][0] + s1, player_matchup[p2][1] + s2]
        if player == p2:
            player_matchup[p1] = [player_matchup[p1][0] + s2, player_matchup[p1][1] + s1]
    return sorted(player_matchup.items(), key=lambda a: a[1][1] / float(a[1][0] + .0001), reverse=True)


def load_and_unroll_game_list(tourny_map, existing_game_list=None):
    if existing_game_list is None:
        existing_game_list = []
    loaded_games = load_tournament_data(tourny_map)
    game_list_ALL = existing_game_list + loaded_games
    game_list_ALL_unrolled = game_list_unroll(game_list_ALL)
    # game_list_ALL_unrolled_filtered = filter_game_list_by_min_matches(game_list_ALL_unrolled, n=5)
    return game_list_ALL_unrolled


def get_reordered_average_player_elo(game_list, reorderings=100, num_epochs=1):
    player_to_rating_dict_overall = defaultdict(int)
    for i in range(reorderings):
        if i % 10 == 0:
            logging.info(str(i))
        player_to_rating_dict = iterate_through_game_list_update_elo(random.sample(game_list, len(game_list)),
                                                                     num_epochs=num_epochs)
        for k in player_to_rating_dict.keys():
            player_to_rating_dict_overall[k] += player_to_rating_dict[k]
    return {k: v / float(reorderings) for k, v in player_to_rating_dict_overall.items()}


def get_num_games(game_list):
    player_to_game_count = defaultdict(int)
    for game in game_list:
        p1, s1, p2, s2 = game
        player_to_game_count[p1] += s1 + s2
        player_to_game_count[p2] += s1 + s2
    return player_to_game_count


def get_and_filter_player_list(game_list, top=None, min_win_loss=0):
    player_to_play_count = defaultdict(int)
    for game in game_list:
        if len(game) == 4:
            p1, s1, p2, s2 = game
            player_to_play_count[p1] += 1
            player_to_play_count[p2] += 1
        else:
            logging.warning("get_and_filter_player_list failed on {}".format(str(game)))
    player_to_play_count_sorted = sorted(player_to_play_count.items(), key=lambda a: a[1], reverse=True)
    if top is None:
        top_n_players_sets_played = [player for player, rating in player_to_play_count_sorted]
    else:
        top_n_players_sets_played = [player for player, rating in player_to_play_count_sorted[:top]]
    # create the matchups list for each player
    player_to_matchup_list = defaultdict(lambda: defaultdict(lambda: np.array([0, 0])))
    for game in game_list:
        if len(game) == 4:
            p1, s1, p2, s2 = game
            player_to_matchup_list[p1][p2] += np.array([s1, s2])
            player_to_matchup_list[p2][p1] += np.array([s2, s1])
        else:
            logging.warning("get_and_filter_player_list part 2 failed on {}".format(str(game)))
    # remove people who haven't won or lost at least 10 games each.
    bad_player_set = set()
    for p1, v in player_to_matchup_list.items():
        if sum([scores[0] for p2, scores in v.items()]) < min_win_loss or sum(
                [scores[1] for p2, scores in v.items()]) < min_win_loss:
            bad_player_set.add(p1)
    players_with_win_loss_thresh = [player for player in top_n_players_sets_played if player not in bad_player_set]
    return list(set(top_n_players_sets_played).intersection(players_with_win_loss_thresh))  # redundant


def get_matchups(game_list, player_list):
    player_to_idx = {player: i for i, player in enumerate(player_list)}
    player_set = set(player_list)
    matchups = defaultdict(lambda: [0, 0])
    for game in game_list:
        if len(game) == 4:
            p1, s1, p2, s2 = game
            if p1 in player_set and p2 in player_set:
                tmp_track_dict = {p1: s1, p2: s2}
                player_pair = tuple(sorted([p1, p2]))
                matchups[player_pair][0] += int(tmp_track_dict[player_pair[0]])
                matchups[player_pair][1] += int(tmp_track_dict[player_pair[1]])
        else:
            logging.warning("get_matchups failed on {}".format(str(game)))
    return [[player_to_idx[matchup_player_1], player_to_idx[matchup_player_2], matchup_score_1, matchup_score_2] for
            (matchup_player_1, matchup_player_2), (matchup_score_1, matchup_score_2) in matchups.items()], player_to_idx


# class LossEq(nn.Module):
#     def __init__(self, player_list, matchups, player_to_rating_dict_overall=None):
#         super().__init__()
#         if player_to_rating_dict_overall is not None:
#             rating_list = np.array([float(player_to_rating_dict_overall[player]) if player in player_to_rating_dict_overall else 1000.0  for player in player_list])
#             rating_list_normalized = ((rating_list - np.min(rating_list))/np.mean(rating_list))*3+1
#             rating_list_normalized_exp = np.power(np.e, rating_list_normalized)
#             self.weights = nn.Parameter(torch.Tensor(rating_list_normalized_exp))
#         else:
#             self.weights = nn.Parameter(torch.Tensor([400.0 for _ in range(len(player_list))]))
#         #self.weights = nn.Parameter(torch.Tensor([100.0 for _ in range(num_players)]))
#         s1_arr = np.array([float(matchup[2]) for matchup in matchups])
#         s2_arr = np.array([float(matchup[3]) for matchup in matchups])
#         total_matches_arr = s1_arr + s2_arr
#         self.p1_idx_arr = np.array([matchup[0] for matchup in matchups])
#         self.p2_idx_arr = np.array([matchup[1] for matchup in matchups])
#         self.s1_tensor = torch.tensor(s1_arr)
#         self.total_matches_tensor = torch.tensor(total_matches_arr)
#         #self.loss = 0
#         # for matchup in matchups:
#         #     p1_rating = self.weights[matchup[0]]
#         #     p2_rating = self.weights[matchup[1]]
#         #     p1_estimated_winning_prob = p1_rating/(p1_rating + p2_rating)
#         #     self.loss += torch.distributions.binomial.Binomial(float(matchup[2]) + float(matchup[3]), p1_estimated_winning_prob).log_prob(torch.tensor([float(matchup[2])]))
#     def forward(self):
#         expected_prob_p1_win_tensor = self.weights[self.p1_idx_arr]/(self.weights[self.p1_idx_arr] + self.weights[self.p2_idx_arr])
#         loss_elem_vect = torch.distributions.binomial.Binomial(self.total_matches_tensor, expected_prob_p1_win_tensor).log_prob(self.s1_tensor)
#         loss_val = -torch.sum(loss_elem_vect)
#         return loss_val, loss_elem_vect.detach().cpu().numpy()



class LossEq(nn.Module):
    def __init__(self, player_list, matchups, player_to_rating_dict_overall=None):
        # https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model
        super().__init__()
        # torch.set_default_dtype(torch.float64)
        if player_to_rating_dict_overall is not None:
            rating_list = np.array(
                [float(player_to_rating_dict_overall[player]) if player in player_to_rating_dict_overall else 1000.0 for
                 player in player_list])
            rating_list_normalized = ((rating_list - np.min(rating_list)) / np.mean(rating_list)) * 3 + 1
            rating_list_normalized_exp = np.power(np.e, rating_list_normalized)
            self.weights = nn.Parameter(torch.Tensor(rating_list_normalized_exp))
        else:
            self.weights = nn.Parameter(torch.Tensor([1.0 for _ in range(len(player_list))]))
        # self.weights = nn.Parameter(torch.Tensor([100.0 for _ in range(num_players)]))
        s1_arr = np.array([float(matchup[2]) for matchup in matchups])
        s2_arr = np.array([float(matchup[3]) for matchup in matchups])
        total_matches_arr = s1_arr + s2_arr
        self.p1_idx_arr = np.array([matchup[0] for matchup in matchups])
        self.p2_idx_arr = np.array([matchup[1] for matchup in matchups])
        self.s1_tensor = torch.tensor(s1_arr)
        self.total_matches_tensor = torch.tensor(total_matches_arr)
        # self.loss = 0
        # for matchup in matchups:
        #     p1_rating = self.weights[matchup[0]]
        #     p2_rating = self.weights[matchup[1]]
        #     p1_estimated_winning_prob = p1_rating/(p1_rating + p2_rating)
        #     self.loss += torch.distributions.binomial.Binomial(float(matchup[2]) + float(matchup[3]), p1_estimated_winning_prob).log_prob(torch.tensor([float(matchup[2])]))

    def forward(self):
        expected_prob_p1_win_tensor = torch.exp(self.weights[self.p1_idx_arr]) / (
        torch.exp(self.weights[self.p1_idx_arr]) + torch.exp(self.weights[self.p2_idx_arr]))
        # expected_prob_p1_win_tensor = self.weights[self.p1_idx_arr]/(self.weights[self.p1_idx_arr] + self.weights[self.p2_idx_arr])
        # expected_prob_p1_win_tensor = torch.exp(self.weights[self.p1_idx_arr] - self.weights[self.p2_idx_arr])
        # try:
        loss_elem_vect = torch.distributions.binomial.Binomial(self.total_matches_tensor,
                                                               expected_prob_p1_win_tensor).log_prob(self.s1_tensor)
        # except:
        #     for i, num in enumerate(expected_prob_p1_win_tensor.detach().cpu().numpy()):
        #         if not (0 < num <= 1):
        #            print(i)
        #            print(self.weights[self.p1_idx_arr[i]])
        #            print(self.weights[self.p2_idx_arr[i]])
        #            print(expected_prob_p1_win_tensor[i] <= 1)
        #     raise ValueError("")
        loss_val = -torch.sum(loss_elem_vect)
        return loss_val, loss_elem_vect.detach().cpu().numpy()


def optimize_loss_eq(player_list, matchups, iters=10000):
    loss_eq = LossEq(player_list, matchups)
    opt = torch.optim.Adam([loss_eq.weights], lr=0.1)
    for i in range(iters):
        # try:
        opt.zero_grad()
        z, loss_vect = loss_eq()
        z.backward()
        opt.step()
        with torch.no_grad():
            _ = loss_eq.weights.clamp_(torch.tensor(1.0), None)
            # except:
            #     break
    return loss_eq


def get_player_scores(player_list, matchups, iters=10000):
    # Run the algorithm, we basically just set up the loss eq structure then we use ADAM to run grad descent
    # the clamp forces the weights to be >=1.0 making this projected gradient descent.  Nothing to interesting here,
    # the only interesting part is the setup of the loss function in "LossEq", the below is just a normal grad descent.
    # Note that we are optimizing a fixed loss function not a SGD on a model where data over batches changes the loss function etc,
    # so only the weight variable (the player scores) changes across the loop
    loss_eq = optimize_loss_eq(player_list, matchups)
    ranking_scores = loss_eq.weights.detach().cpu().numpy()
    player_to_rating_dict = {player: rating for player, rating in zip(player_list, ranking_scores)}
    return player_to_rating_dict


def get_player_scores_wrapper(input_args):
    return get_player_scores(input_args['player_list'], input_args['matchups'], iters=input_args['iters'])


def get_player_variances(player_list, matchups, bootstrap_count=100, parallel=True):
    # run the same as the above but with our data bootstrap resampled (with replacement).
    # Keep track of all scores for each player in player_to_rating_dict_boot_list
    if parallel:
        input_args_list = []
        for bootidx in range(bootstrap_count):
            matchups_boot = random.choices(matchups, k=len(matchups))
            input_args_list.append({'player_list': player_list, 'matchups': matchups_boot, 'iters': 10000})
        MAX_WORKERS = mp.cpu_count()
        CHUNK_SIZE = max(int(len(input_args_list) / MAX_WORKERS), 1)
        logging.info(str(MAX_WORKERS))
        logging.info(str(CHUNK_SIZE))
        ctx = mp.get_context('spawn')
        pool = ctx.Pool(processes=MAX_WORKERS)
        results = tqdm(
            pool.imap_unordered(get_player_scores_wrapper, input_args_list, chunksize=CHUNK_SIZE),
            total=len(input_args_list),
        )
        pool.close()
        player_to_rating_dict_boot_list = list(results)
    else:
        player_to_rating_dict_boot_list = []
        for bootidx in range(bootstrap_count):
            logging.info(str(bootidx))
            matchups_boot = random.choices(matchups, k=len(matchups))
            player_to_rating_dict = get_player_scores(player_list, matchups_boot, iters=10000)
            player_to_rating_dict_boot_list.append(player_to_rating_dict)
    return player_to_rating_dict_boot_list


def get_player_score_and_variance(player_list, matchups, bootstrap_count=100):
    # combine first and second run into one dict with the final results
    # note that with bootstrap resampling method for variance computation
    # you are not supposed to use the mean of your samples as the new score around which the variance is computed
    # you have to use the normal calculation on the full real dataset (cmu stats has a good explanation of this)
    player_to_rating_dict_real = get_player_scores(player_list, matchups)
    player_to_rating_dict_boot_list = get_player_variances(player_list, matchups, bootstrap_count=bootstrap_count)
    player_name_to_tot_and_std = {}
    for player_name in player_to_rating_dict_boot_list[0]:
        player_name_to_tot_and_std[player_name] = [player_to_rating_dict_real[player_name], np.std(
            [player_to_rating_dict_boot_list[boot_i][player_name] for boot_i in range(bootstrap_count)])]
    # sort the dict by results
    player_name_to_tot_and_std_sorted = sorted(player_name_to_tot_and_std.items(), key=lambda a: a[1][0], reverse=True)
    player_name_to_tot_and_std_sorted_reformat = [[player_name, score, std_val] for player_name, [score, std_val] in
                                                  player_name_to_tot_and_std_sorted]
    return player_name_to_tot_and_std_sorted_reformat


def enforce_prior(matchup, prior):
    p1, p2, s1, s2 = matchup
    s2 = s2 * prior
    s1 = s1 * prior
    if s1 > s2:
        s1 = s1 + 1
    elif s1 < s2:
        s2 = s2 + 1
    return [p1, p2, s1, s2]


def run_h2h_ratio_ranking(all_games, top_player_number=None, min_win_loss=0, sets=False, prior=None):
    if sets:
        all_games = convert_game_score_to_winlose_set(all_games)
    # If we want to run a fast test we can make top equal n to get just the n player with the most games played
    player_list = get_and_filter_player_list(all_games, top=top_player_number, min_win_loss=min_win_loss)
    # get the final set of matchups for the set of players we want.  dumb of me to have games as p1 s1 p2 s2 and matchup as p1 p2 s1 s2
    matchups, player_to_idx = get_matchups(all_games, player_list)
    if prior is not None:
        print("FORCING PRIOR: {}".format(str(prior)))
        matchups = [enforce_prior(matchup, prior) for matchup in matchups]
    with open(Path().home() / "matchups.json", 'w') as f:
        json.dump(matchups, f)
    player_name_to_tot_and_std_sorted = get_player_score_and_variance(player_list, matchups)
    return player_name_to_tot_and_std_sorted


def run_elo_ranking(all_games, sets=False):
    # Convert sets into single games for elo computation (not needed for other alg)
    if sets:
        game_list_unrolled = convert_game_score_to_winlose_set(all_games)
    else:
        game_list_unrolled = game_list_unroll(all_games)
    # #Run elo computation.  We do 1000 random orderings and 100 runs through to widen scores and even out the problem elo has with being order dependent
    player_to_rating_dict = get_reordered_average_player_elo(game_list_unrolled, reorderings=1000, num_epochs=5)
    player_rating_sorted = sorted(player_to_rating_dict.items(), key=lambda a: a[1], reverse=True)
    return player_rating_sorted
    # #Sort and display the results
    # display_player_rating(player_to_rating_dict, top=50)


def get_rankings(start_date=None, end_date=None, top_player_number=None, min_win_loss=0,
                 rankings_to_run=("elo_games", "elo_sets", "h2h_ratio_games", "h2h_ratio_sets"),
                 refresh_artifacts=False, prior=None):
    if refresh_artifacts:
        get_recent_artifacts()
    tournament_to_date_dict = load_json(ALL_TOURNAMENTS_DATES_FILE)
    game_dict = load_json(ALL_TOURNAMENTS_GAMES_FILE)
    selected_tournament_urls = get_tournaments_from_date_range(tournament_to_date_dict, start_date=start_date,
                                                               end_date=end_date)
    logging.info("Selected the following tournaments from date range {} to {}:".format(start_date, end_date))
    logging.info("\n".join(selected_tournament_urls))
    all_games = get_game_list_from_list_of_tournaments(game_dict, selected_tournament_urls)
    logging.info("Finished processing all {} games".format(str(len(all_games))))
    all_rankings_dict = {}
    if "elo_games" in rankings_to_run:
        logging.info("Started elo computation on games")
        score_table = run_elo_ranking(all_games, sets=False)
        # df = pd.DataFrame(score_table, columns = ['Player', 'Score'])
        all_rankings_dict["elo_games"] = score_table
        logging.info("Finished elo computation on games")
    if "elo_sets" in rankings_to_run:
        logging.info("Started elo computation on sets")
        score_table = run_elo_ranking(all_games, sets=True)
        # df = pd.DataFrame(score_table, columns = ['Player', 'Score'])
        all_rankings_dict["elo_sets"] = score_table
        logging.info("Finished elo computation on sets")
    if "h2h_ratio_games" in rankings_to_run:
        logging.info("Started h2h_ratio computation on games")
        score_table = run_h2h_ratio_ranking(all_games, top_player_number=top_player_number, min_win_loss=min_win_loss,
                                            sets=False)
        # df = pd.DataFrame(score_table, columns = ['Player', 'Score', 'Std. Dev.'])
        all_rankings_dict["h2h_ratio_games"] = score_table
        logging.info("Finished h2h_ratio computation on games")
    if "h2h_ratio_sets" in rankings_to_run:
        logging.info("Started h2h_ratio computation on sets")
        score_table = run_h2h_ratio_ranking(all_games, top_player_number=top_player_number, min_win_loss=min_win_loss,
                                            sets=True, prior=prior)
        # df = pd.DataFrame(score_table, columns = ['Player', 'Score', 'Std. Dev.'])
        all_rankings_dict["h2h_ratio_sets"] = score_table
        logging.info("Finished h2h_ratio computation on sets")
    return all_rankings_dict, selected_tournament_urls, dict(top_player_number=top_player_number,
                                                             min_win_loss=min_win_loss)


def check_if_uri_exists(s3_client, bucket, key):
    try:
        s3_client.head_object(Bucket=bucket, Key=key)
    except ClientError as e:
        return int(e.response['Error']['Code']) != 404
    return True


def run_new_ranking_and_backup(start_date, end_date, top_player_number=None, min_win_loss=1, overwrite=False,
                               rankings_to_run=("elo_games", "elo_sets", "h2h_ratio_games"), prior=None):
    get_recent_artifacts()
    start_date = datetime.datetime.strptime(start_date, '%m/%d/%Y')
    end_date = datetime.datetime.strptime(end_date, '%m/%d/%Y')
    tournament_to_date_dict = load_json(ALL_TOURNAMENTS_DATES_FILE)
    game_dict = load_json(ALL_TOURNAMENTS_GAMES_FILE)
    selected_tournament_urls = get_tournaments_from_date_range(tournament_to_date_dict, start_date=start_date,
                                                               end_date=end_date)
    uniq_tourneyset_str = ",".join(
        sorted(["/".join([t.split("/")[4], t.split("/")[6]]) for t in selected_tournament_urls]))
    uniq_tourneyset_key = hashlib.sha256(uniq_tourneyset_str.encode()).hexdigest()
    tmp_results_file = Path().home() / 'tmp_results_file.json'
    results_s3_uri = f"data/results_cache/{uniq_tourneyset_key}.json"
    if tmp_results_file.exists():
        tmp_results_file.unlink()
    if overwrite or not check_if_uri_exists(s3_client, 'smash-ranking', results_s3_uri):
        print("No cached version exists for this run, recomputing.")
        rankings_dict, selected_tournament_urls, config = get_rankings(start_date=start_date, end_date=end_date,
                                                                       top_player_number=top_player_number,
                                                                       min_win_loss=min_win_loss,
                                                                       rankings_to_run=rankings_to_run,
                                                                       refresh_artifacts=True, prior=prior)
        with open(tmp_results_file, 'w') as f:
            json.dump(rankings_dict, f, cls=NpEncoder)
        s3.Bucket('smash-ranking').upload_file(str(tmp_results_file), results_s3_uri)
    else:
        print("Getting backup file {}".format(str(results_s3_uri)))
        s3.Bucket('smash-ranking').download_file(results_s3_uri, str(tmp_results_file))
        with open(tmp_results_file, 'r') as f:
            rankings_dict = json.load(f)
        config = {}
    return rankings_dict, selected_tournament_urls, config

# #Load the data
# # games_before_quarantine = load_tournament_data(PRE_COVID_tournament_url_to_page_num)
# # games_after_quarantine_120821 = load_tournament_data(POST_COVID_tournament_url_to_page_num)
# games_before_quarantine = load_games('/Users/deaxman/Downloads/smash_before_quarantine.csv')
# games_after_quarantine = load_games('/Users/deaxman/Downloads/smash_after_quarantine.tsv')
# games_after_quarantine_120821 = load_games('/Users/deaxman/Downloads/smash_after_quarantine_120821.tsv')


# jp_matches = load_tournament_data(jp_tournaments)



# page = requests.get('https://smash.gg/tournament/the-smash-world-tour-championships/event/ultimate-championships/matches?page=1', timeout=None)
# soup = BeautifulSoup(page.content, "html.parser")
# job_elements = soup.find_all("table", class_="regionWrapper-APP_TOURNAMENT_PAGE-FeatureCanvas-MuiTable-root")
#             table = job_elements[0]

# https://smash.gg/tournament/the-smash-world-tour-championships/event/ultimate-championships/matches
# write_games('/Users/deaxman/Downloads/jp_matches.tsv', jp_matches)

# swt_matches = load_tournament_data(SWT_data)

# post_swt_post_quarantine = games_after_quarantine_120821 + swt_matches












