
curl -s "https://${ApiGatewayRestApi}.execute-api.us-east-1.amazonaws.com/prod/get_ranking?ranking_to_run=trueskill&tier_options=P,S%2B,S,A%2B&start_date=2020-03-16T00:00:00&end_date=2024-01-16T00:00:00&evaluation_level=sets" | jq .

curl -s "https://${ApiGatewayRestApi}.execute-api.us-east-1.amazonaws.com/prod/get_ranking?ranking_to_run=bradleyterry&tier_options=P,S%2B,S,A%2B&start_date=2020-07-16T00:00:00&end_date=2024-01-16T00:00:00&evaluation_level=sets" | jq .


curl -s "https://${ApiGatewayRestApi}.execute-api.us-east-1.amazonaws.com/prod/get_ranking?ranking_to_run=elo&tier_options=P,S%2B,S,A%2B&start_date=2019-01-01T00:00:00&end_date=2023-12-30T00:00:00&evaluation_level=sets" | jq .

curl -s "https://${ApiGatewayRestApi}.execute-api.us-east-1.amazonaws.com/prod/get_ranking?ranking_to_run=trueskill&tier_options=P,S%2B,S,A%2B&start_date=2022-07-01T00:00:00&end_date=2023-11-06T00:00:00&evaluation_level=sets" | jq .

trueskill 34.65
bt 23.41
elo 3.71
glicko2 5.49




trueskill

| Player | Mean Rating | Relative Uncertainty |
|--------|-------------|----------|
| ZETA | あcola | 46.58 | 1.93 |
| LG | Sonix | 46.00 | 1.78 |
| FaZe | Sparg0 | 45.88 | 1.89 |
| FENNEL | ミーヤー | 45.28 | 1.84 |
| LG | Tweek | 43.85 | 1.73 |
| Nairo | 43.23 | 1.82 |
| LG | MkLeo | 42.93 | 1.77 |
| SHADIC | 42.88 | 1.76 |
| Liquid | Riddles | 42.71 | 1.76 |
| MSU | Onin | 42.37 | 1.81 |
| DDee | 42.28 | 2.00 |
| RC | Shuton | 42.23 | 1.75 |
| ShinyMark | 42.14 | 1.78 |
| sixth isthmus | 42.08 | 6.34 |
| Solary | Glutonny | 42.05 | 1.79 |
| Moist | Light | 41.97 | 1.70 |
| LG | Maister | 41.75 | 1.71 |
| Zomba | 41.73 | 1.75 |
| DFM | zackray | 41.72 | 1.76 |
| E36 | Hurt | 41.71 | 1.81 |
| Samsora | 41.64 | 1.78 |
| Ouch!? | 41.54 | 1.82 |
| CR | ProtoBanham | 41.22 | 1.75 |
| Moist | Kola | 41.21 | 1.71 |
| Dabuz | 41.19 | 1.72 |
| VGY | Sisqui | 41.16 | 1.80 |
| PSK | ETN | WaKa | 41.14 | 1.80 |
| DTL | Syrup | 41.13 | 1.73 |
| Asimo | 41.13 | 1.71 |
| Rob sucks | Desmona | 41.07 | 5.53 |
| SOL | らる | 41.02 | 1.73 |


BT



ELO

| Player | Mean Rating | Relative Uncertainty |
|--------|-------------|----------|
| ZETA | あcola | 2415.12 | 4.21 |
| FENNEL | ミーヤー | 2353.02 | 3.03 |
| FaZe | Sparg0 | 2339.91 | 2.71 |
| LG | Sonix | 2338.54 | 3.91 |
| LG | Tweek | 2239.69 | 3.05 |
| RC | Shuton | 2211.70 | 2.48 |
| LG | MkLeo | 2206.51 | 2.52 |
| Nairo | 2203.33 | 11.36 |
| E36 | Hurt | 2199.27 | 5.33 |
| SHADIC | 2194.61 | 4.57 |
| DFM | zackray | 2193.76 | 5.75 |
| Liquid | Riddles | 2179.63 | 3.12 |
| Solary | Glutonny | 2177.90 | 2.23 |
| SOL | らる | 2171.27 | 4.73 |
| CR | ProtoBanham | 2170.42 | 7.09 |
| MSU | Onin | 2165.65 | 5.36 |
| LG | Maister | 2161.42 | 3.21 |
| Moist | Light | 2159.30 | 1.86 |
| Asimo | 2155.61 | 2.56 |
| ZETA | Tea | 2154.81 | 3.67 |




glicko:

| Player | Mean Rating | Relative Uncertainty |
|--------|-------------|----------|
| ZETA | あcola | 2601.17 | 157.17 |
| LG | Sonix | 2571.37 | 142.72 |
| FaZe | Sparg0 | 2567.84 | 159.06 |
| FENNEL | ミーヤー | 2558.83 | 152.07 |
| LG | Tweek | 2484.82 | 136.77 |
| Moist | Light | 2450.25 | 137.25 |
| LG | MkLeo | 2439.85 | 138.97 |
| Asimo | 2419.97 | 136.80 |
| SHADIC | 2410.39 | 140.91 |
| Liquid | Riddles | 2404.87 | 138.99 |
| Lima | 2402.59 | 133.94 |
| SOL | らる | 2402.07 | 143.00 |
| LG | Maister | 2390.85 | 133.80 |
| DFM | zackray | 2387.18 | 138.73 |
| RC | Shuton | 2383.82 | 145.98 |
| ShinyMark | 2377.55 | 142.85 |
| DTL | Syrup | 2363.06 | 139.47 |
| MSU | Onin | 2359.25 | 144.49 |
| BMS | crêpe salée | 2357.30 | 145.43 |
| Solary | Glutonny | 2353.03 | 141.66 |
| DDee | 2348.35 | 148.34 |
| Ouch!? | 2346.99 | 143.64 |
| ZETA | Tea | 2345.51 | 135.30 |
| iXA | Yaura | 2343.40 | 140.63 |
| Moist | Kola | 2341.85 | 138.17 |
| E36 | Hurt | 2337.29 | 145.91 |
| sixth isthmus | 2328.89 | 331.49 |
| Zomba | 2328.16 | 140.79 |
| PSK | ETN | WaKa | 2327.52 | 145.35 |
| VGY | Sisqui | 2324.35 | 144.70 |
| AREA310 | ドラ右 | 2314.68 | 144.25 |
| Dabuz | 2308.27 | 134.71 |
| Revo | Yoshidora | 2304.67 | 138.32 |
| Nairo | 2304.10 | 136.93 |
| Marss | 2300.60 | 135.78 |
| CR | ProtoBanham | 2296.37 | 141.69 |
| Wrath | 2287.88 | 140.20 |
| CN / EFG | AlanDiss | 2281.64 | 139.92 |
| Raflow | 2278.62 | 138.12 |
| DLT/CS3 | MKBigBoss | 2276.83 | 138.00 |





aws logs filter-log-events \
    --log-group-name "/aws/lambda/SmashRankerFunction" \
    --start-time $(( $(date +%s) * 1000 - 40000 )) \
    --query 'events[*].{timestamp:timestamp, message:message}' \
    --output text

ts = query_tournaments(tier_options=("P", "S+", "S", "A+", "A"), start_date='2018-06-16T00:00:00', end_date='2026-11-07T00:00:00')
all_s3_files_to_download = ["{}-{}.json".format(result["tourney_slug"], result["event_slug"]) for result in ts]
download_s3_files(all_s3_files_to_download, overwrite=False)
all_uncertainty_and_actual_diff_dict = {}
tournament_exp_range = 1
print(len(all_s3_files_to_download))
ranking_to_run = "trueskill"
all_uncertainty_and_actual_diff = []
for batch_size in range(2, 10):
    for i in range(0, len(all_s3_files_to_download)-batch_size, 3):
        print(f"{i}/{len(all_s3_files_to_download)-batch_size}")
        first_tournaments = all_s3_files_to_download[i:i + batch_size - tournament_exp_range]
        all_tournaments = all_s3_files_to_download[i:i + batch_size]
        first_sets = get_all_sets_from_tournament_files(first_tournaments)
        all_sets = get_all_sets_from_tournament_files(all_tournaments)
        ratings_1, id_to_player_name_1, player_to_id_1 = get_player_rating(first_sets, ranking_to_run=ranking_to_run,
                                                                     evaluation_level="sets")
        ratings_2, id_to_player_name_2, player_to_id_2 = get_player_rating(all_sets, ranking_to_run=ranking_to_run,
                                                                     evaluation_level="sets")
        ratings_1 = sorted(ratings_1, key=lambda a: a["rating"], reverse=True)[:30]
        ratings_2 = sorted(ratings_2, key=lambda a: a["rating"], reverse=True)[:75]
        ratings_2_dict = {r["player"]: r["rating"] for r in ratings_2}
        for r in ratings_1:
            player_id = r["player"]
            initial_rating = r["rating"]
            initial_uncertainty = r["uncertainty"]
            if player_id in ratings_2_dict:
                final_rating = ratings_2_dict[player_id]
                actual_diff = final_rating - initial_rating
                all_uncertainty_and_actual_diff.append([initial_uncertainty, abs(actual_diff)])
all_uncertainty_and_actual_diff_dict[ranking_to_run] = all_uncertainty_and_actual_diff



import math

# Define the number of bins
num_bins = 40  # Change this to the desired number of bins
ranking_to_run = "trueskill"
# Calculate the range of point[0] values
min_value = min(point[0] for point in all_uncertainty_and_actual_diff_dict[ranking_to_run])
max_value = max(point[0] for point in all_uncertainty_and_actual_diff_dict[ranking_to_run])
bin_width = (max_value - min_value) / num_bins
# Calculate the 99th percentile for point[1] values in each bin
for i in range(num_bins):
    lower_bound = min_value + i * bin_width
    upper_bound = lower_bound + bin_width
    filtered_points = [point for point in all_uncertainty_and_actual_diff_dict[ranking_to_run] if lower_bound < point[0] <= upper_bound]
    if filtered_points:
        # Sort and get the 99th percentile value of point[1] in this bin
        percentile_value = sorted([point[1] for point in filtered_points])[int(0.9 * len(filtered_points))]
        x = (upper_bound + upper_bound)/2
        #x_if_sqrt = 2000 / math.sqrt((2000 / x))
        x_ratio = percentile_value/x
        #x_if_sqrt_ratio = percentile_value/x_if_sqrt
        print(
            f"{x},{x_ratio}, Bin {i + 1} ({lower_bound:.2f} to {upper_bound:.2f}) {len(filtered_points)}: 99th percentile of point[1] is {percentile_value}")
    else:
        print(f"Bin {i + 1} ({lower_bound:.2f} to {upper_bound:.2f}): No data")





for i in range(2, 11):
    filtered_points = [point for point in all_uncertainty_and_actual_diff if (i < point[0]) and (point[0] < i+1)]
    print(i, sorted([point[1] for point in filtered_points])[int(0.99*len(filtered_points))])


# Count how many of these points also have the second value less than the first value
matching_points = [point for point in filtered_points if point[1] < point[0]]

# Calculate the proportion
proportion = len(matching_points) / len(filtered_points) if filtered_points else 0

print("Proportion:", proportion)

import matplotlib.pyplot as plt
top_points = sorted(all_uncertainty_and_actual_diff, key = lambda a: a[1])[int(-0.05*len(all_uncertainty_and_actual_diff)):]
x_values = [point[0] for point in top_points]
y_values = [point[1] for point in top_points]


plt.figure(figsize=(8, 6))
plt.hist2d(x_values, y_values, bins=50, cmap='Blues')
plt.colorbar(label='Count')
plt.xlabel('Initial Uncertainty')
plt.ylabel('Absolute Rating Change')
plt.title('2D Histogram of Uncertainty vs. Rating Change')
plt.xlim(2, 10)
plt.ylim(0, 5)
plt.show(block=True)

#Create the scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(x_values, y_values, s=10, alpha=0.2)
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Scatter Plot of Points')
plt.grid(True)
#plt.xlim(50, 100)
plt.show(block=True)

plt.figure(figsize=(8, 6))
plt.hexbin(x_values, y_values, gridsize=50, cmap='Blues')
plt.colorbar(label='Count')
plt.xlabel('Initial Uncertainty')
plt.ylabel('Absolute Rating Change')
plt.title('Hexbin Plot of Uncertainty vs. Rating Change')
plt.grid(True)
plt.show()


plt.figure(figsize=(8, 6))
plt.hist(y_values, bins='auto', range=(0, .2), color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel('Y Values')
plt.ylabel('Frequency')
plt.title('Distribution of Y Values (0-400)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show(block=True)









Make a very good looking react website that collects information from the user at the top in a series of fields (Tier (drop down of selectable "P", "S+", "S", "A+", "A", "B+", "B", "C" where multiple can be selected, start_date (default to Nov 1 2018 if not selected), end_date (default to today if not selected), ranking_to_run (drop down of either elo, or trueskill), and evaluation_level (a choice of either "sets" or "games"))

Whenever Tier, start_date, or end_date are changed, a query like this will be sent by the website:

curl -X POST "https://1234567.execute-api.us-east-1.amazonaws.com/prod/query_tournaments" \
-H "x-api-key: smash_ranker_api_secret_key" \
-H "Content-Type: application/json" \
-d '{
    'tier_options': ("P", "S+", "S", "A+", "A")
    'start_date': '2018-07-16T00:00:00'
    'end_date':'2024-11-06T00:00:00'
    }'

This will return a list of dicts where each dict has a field "tourney_slug".  We want to display the tourney_slug for each item in a nice, clean, pretty vertical list.  Picture the fields along the top and then the section below the fields split into left half and right half.  The left half will have this list of tourney slugs, the right will have a ranking of players (we'll talk about this later).

Also just under the fields (and above the tourney slug list/ranking left right split section) is a pretty looking green button "Compute Ranking".  When pressed, a request like this will be sent:

curl -X POST "https://1234567.execute-api.us-east-1.amazonaws.com/prod/get_ranking" \
-H "x-api-key: smash_ranker_api_secret_key" \
-H "Content-Type: application/json" \
-d '{
    'ranking_to_run': 'elo'
    'tier_options': ("P", "S+", "S", "A+", "A")
    'start_date': '2018-07-16T00:00:00'
    'end_date':'2024-11-06T00:00:00'
    'evaluation_level': 'sets'
    }'


the response will look like this:
[{"player": "Mkleo", "score": 2000, "uncertainty": 50}, {"player": "Tweek", "score": 1800, "uncertainty": 150}, {"player": "Shuton", "score": 1600, "uncertainty": 50}]


On the right side of the split lower half, display this list of rankings in a pretty table. Show each player, their score, and their score variance for the top 100 players.  The column names should be "Player", "Mean Rating", and "Relative Uncertainty" respectively.

Above this table, show the parameters for this ranking (the date range, selected tiers, ranking type, and evaluation level).

Implement stateful URL encoding so that when a user presses the button, the form data and page state are encoded as URL parameters. This way, the URL becomes shareable, and anyone visiting it will see the same pre-filled form and state.

Output the file name and exact contents of each file in the react app.  Ask any questions needed before starting.






d = {}
for i in range(100000):
    if i%100 == 0:
        print(i)
    d[tuple([f"supernova-2024/event/ultimate-1v1-singles{i}"]*400)] = {(str(p)+str(i)): p for p in range(100)}



from pympler import asizeof

# Using `asizeof` from pympler to calculate the memory size in MB
dict_most_accurate_size_mb = asizeof.asizeof(d) / (1024 * 1024)  # Convert bytes to MB
dict_most_accurate_size_mb



import sys
from collections.abc import Iterable

def get_size_mb(obj, seen=None):
    """
    Recursively estimates the memory usage of a Python object in megabytes.
    This uses the sys.getsizeof() function to get the size of the object.
    """
    seen = seen or set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    seen.add(obj_id)
    size = sys.getsizeof(obj)
    if isinstance(obj, dict):
        size += sum(get_size_mb(k, seen) + get_size_mb(v, seen) for k, v in obj.items())
    elif isinstance(obj, (list, tuple, set, Iterable)) and not isinstance(obj, (str, bytes, bytearray)):
        size += sum(get_size_mb(item, seen) for item in obj)
    return size / (1024 * 1024)


get_size_mb(d)




query PhaseGroupSets($phaseGroupId: ID!, $page:Int!, $perPage:Int!){
  phaseGroup(id:$phaseGroupId){
    sets(
      page: $page
      perPage: $perPage
      sortType: STANDARD
    ){
      pageInfo{
        total
      }
      nodes{
        slots{
          standing{
          placement
          stats{
            score{
              value
            }
          }
          }
          entrant{
            name
            participants{
              player{
                user{
                  discriminator
                }
              }
            }
          }
        }
      }
    }
  }
}



{
  "phaseGroupId": 2652523,
  "page": 1,
  "perPage": 10
}










2024-11-03 21:40:58,785 - INFO - Saved tournament data for 'ludwig-smash-invitational' to file 'ludwig-smash-invitational-ultimate-singles-main-event.json'.
2024-11-03 21:40:59,263 - INFO - Uploaded 'ludwig-smash-invitational-ultimate-singles-main-event.json' to S3 bucket 'smash-ranking-tournament-data' and deleted local file.
2024-11-03 21:40:59,366 - INFO - Updated DynamoDB table 'smash-ranking-tournament-table' with tournament 'ludwig-smash-invitational'.


2024-11-03 21:41:19,052 - INFO - Retrieved details for tournament 'couchwarriors-vic-march-ranking-battle-2021-smash': Name=CouchWarriors VIC March Ranking Battle (2021) - Smash, Date=2021-03-27 00:00:00, Sets=196.
2024-11-03 21:41:19,060 - INFO - Saved tournament data for 'couchwarriors-vic-march-ranking-battle-2021-smash' to file 'couchwarriors-vic-march-ranking-battle-2021-smash-smash-ultimate-singles.json'.
2024-11-03 21:41:19,833 - INFO - Uploaded 'couchwarriors-vic-march-ranking-battle-2021-smash-smash-ultimate-singles.json' to S3 bucket 'smash-ranking-tournament-data' and deleted local file.
2024-11-03 21:41:19,943 - INFO - Updated DynamoDB table 'smash-ranking-tournament-table' with tournament 'couchwarriors-vic-march-ranking-battle-2021-smash'.



2024-11-03 21:41:38,984 - INFO - Retrieved details for tournament 'kowloon-4': Name=九龍-KOWLOON-＃4, Date=2023-01-21 01:00:00, Sets=665.
2024-11-03 21:41:38,998 - INFO - Saved tournament data for 'kowloon-4' to file 'kowloon-4-kowloon-sp.json'.
2024-11-03 21:41:39,840 - INFO - Uploaded 'kowloon-4-kowloon-sp.json' to S3 bucket 'smash-ranking-tournament-data' and deleted local file.
2024-11-03 21:41:39,940 - INFO - Updated DynamoDB table 'smash-ranking-tournament-table' with tournament 'kowloon-4'.



2024-11-03 21:41:47,941 - INFO - Retrieved details for tournament 'rey-del-agua': Name=Rey del Agua, Date=2023-09-23 18:00:00, Sets=210.
2024-11-03 21:41:47,945 - INFO - Saved tournament data for 'rey-del-agua' to file 'rey-del-agua-singles.json'.
2024-11-03 21:41:48,657 - INFO - Uploaded 'rey-del-agua-singles.json' to S3 bucket 'smash-ranking-tournament-data' and deleted local file.
2024-11-03 21:41:48,765 - INFO - Updated DynamoDB table 'smash-ranking-tournament-table' with tournament 'rey-del-agua'.



2024-11-03 21:42:05,936 - INFO - Retrieved details for tournament 'ascension-ii': Name=Ascension II, Date=2019-02-16 16:00:00, Sets=422.
2024-11-03 21:42:05,946 - INFO - Saved tournament data for 'ascension-ii' to file 'ascension-ii-ultimate-singles.json'.
2024-11-03 21:42:06,618 - INFO - Uploaded 'ascension-ii-ultimate-singles.json' to S3 bucket 'smash-ranking-tournament-data' and deleted local file.
2024-11-03 21:42:06,709 - INFO - Updated DynamoDB table 'smash-ranking-tournament-table' with tournament 'ascension-ii'.


2024-11-03 21:43:48,929 - INFO - Retrieved details for tournament 'bit-master-mty-x-thunder-struck-2024': Name=BIT MASTER MTY X THUNDER STRUCK 2024, Date=2024-09-15 01:00:00, Sets=40.
2024-11-03 21:43:48,934 - INFO - Saved tournament data for 'bit-master-mty-x-thunder-struck-2024' to file 'bit-master-mty-x-thunder-struck-2024-super-smash-bros-ultimate.json'.
2024-11-03 21:43:49,518 - INFO - Uploaded 'bit-master-mty-x-thunder-struck-2024-super-smash-bros-ultimate.json' to S3 bucket 'smash-ranking-tournament-data' and deleted local file.
2024-11-03 21:43:49,615 - INFO - Updated DynamoDB table 'smash-ranking-tournament-table' with tournament 'bit-master-mty-x-thunder-struck-2024'.


2024-11-03 21:44:01,271 - INFO - Retrieved details for tournament 'bit-master-mty-22-secret-edition': Name=Bit Master Mty #22: Secret Edition, Date=2024-09-07 19:00:00, Sets=373.
2024-11-03 21:44:01,283 - INFO - Saved tournament data for 'bit-master-mty-22-secret-edition' to file 'bit-master-mty-22-secret-edition-super-smash-bros-ultimate-singles.json'.
2024-11-03 21:44:01,955 - INFO - Uploaded 'bit-master-mty-22-secret-edition-super-smash-bros-ultimate-singles.json' to S3 bucket 'smash-ranking-tournament-data' and deleted local file.
2024-11-03 21:44:02,050 - INFO - Updated DynamoDB table 'smash-ranking-tournament-table' with tournament 'bit-master-mty-22-secret-edition'.


aws s3 rm s3://smash-ranking-tournament-data/ludwig-smash-invitational-ultimate-singles-main-event.json
aws s3 rm s3://smash-ranking-tournament-data/couchwarriors-vic-march-ranking-battle-2021-smash-smash-ultimate-singles.json
aws s3 rm s3://smash-ranking-tournament-data/kowloon-4-kowloon-sp.json
aws s3 rm s3://smash-ranking-tournament-data/rey-del-agua-singles.json
aws s3 rm s3://smash-ranking-tournament-data/ascension-ii-ultimate-singles.json
aws s3 rm s3://smash-ranking-tournament-data/bit-master-mty-x-thunder-struck-2024-super-smash-bros-ultimate.json
aws s3 rm s3://smash-ranking-tournament-data/bit-master-mty-22-secret-edition-super-smash-bros-ultimate-singles.json


aws dynamodb delete-item --table-name smash-ranking-tournament-table --key '{"tourney_slug": {"S": "ludwig-smash-invitational"}}'
aws dynamodb delete-item --table-name smash-ranking-tournament-table --key '{"tourney_slug": {"S": "couchwarriors-vic-march-ranking-battle-2021-smash"}}'
aws dynamodb delete-item --table-name smash-ranking-tournament-table --key '{"tourney_slug": {"S": "kowloon-4"}}'
aws dynamodb delete-item --table-name smash-ranking-tournament-table --key '{"tourney_slug": {"S": "rey-del-agua"}}'
aws dynamodb delete-item --table-name smash-ranking-tournament-table --key '{"tourney_slug": {"S": "ascension-ii"}}'
aws dynamodb delete-item --table-name smash-ranking-tournament-table --key '{"tourney_slug": {"S": "bit-master-mty-x-thunder-struck-2024"}}'
aws dynamodb delete-item --table-name smash-ranking-tournament-table --key '{"tourney_slug": {"S": "bit-master-mty-22-secret-edition"}}'




{
            "eventId": 814979,
            "page": 9,
            "perPage": 40
}

{
            "eventId": 814979,
            "page": 15,
            "perPage": 40
}

{'eventId': 959594, 'page': 6, 'perPage': 40}

lvl-up-expo-2019

{'eventId': 243115, 'page': 10, 'perPage': 40}

{'eventId': 243115, 'page': 23, 'perPage': 40}












google_sheets_url = 'https://docs.google.com/spreadsheets/d/YOUR_GOOGLE_SHEET_ID/edit#gid=SHEET_GID'  # Replace with your Google Sheet URL
sheet_name = 'Tab Name'  # Replace with the name of the sheet to keep
output_file = 'output.xlsx'



s3_bucket = smash_ranking_tournament_data
dynamo_db_table = smash_ranking_tournament_table

# if given a link to the doc
    output_file = 'output_tmp.xlsx'
    download_google_sheet_as_excel(google_sheets_url, sheet_name, output_file)
    all_tournaments_df = process_tournament_file(output_file)
# elif given a path to a folder:
    all_tournaments_df = get_major_tournaments_from_folder(tournament_folder_path)
# if s3 bucket does not exist, then create it
# if ddb does not exist, then create it
for tourney_slug, event_slug, tier in zip(all_tournaments_df["tourney_slug"].to_list(), all_tournaments_df["event_slug"].to_list(), all_tournaments_df["Tier"].to_list()):
    if f"{tourney_slug}.json" not in get_s3_filenames(bucket_name, prefix='') and passes_tier_filters(tier):
        tournament_name, event_start_time, sets = get_all_info_for_tournament(tourney_slug, event_slug)
        save to a file {tourney_slug}.json
        with this:  json.dumps({"link": link, event: "event_slug", "tier": tier, "date": event_start_time, "name": tournament_name, "sets": sets})
        upload this file to the s3 bucket
        update the list of tourney dates, slugs, names, and tiers in ddb (dynamo_db_table) (additionally, in a separate function, give code to pull all of the records (each tournament) in the ddb, or to filter by tier, or between two dates)

"""



# # Display final ratings
# print("Elo Ratings:")
# for player, rating in sorted(elo_ratings.items(), key=lambda a: a[1], reverse=True):
#     print(f"{player}: {rating:.2f}")
#
#
# # Bradley-Terry Ratings as a Markdown Table
# print("## Bradley-Terry Ratings")
# print("| Player | Rating |")
# print("|--------|--------|")
# for player, rating in sorted(zip(players, ratings), key=lambda a: a[1], reverse=True):
#     print(f"| {player} | {rating:.2f} |")
#
# # TrueSkill Ratings as a Markdown Table
# print("\n## TrueSkill Ratings")
# print("| Player | Mu (Rating) | Sigma (Uncertainty) |")
# print("|--------|-------------|--------------------|")
# for player, rating in sorted(ts_ratings.items(), key=lambda a: a[1].mu, reverse=True):
#     print(f"| {player} | {rating.mu:.2f} | {rating.sigma:.2f} |")
#




tournament_folder_path = TOURNAMENT_FOLDER_PATH
all_tournaments_df = get_major_tournaments_from_folder(tournament_folder_path)
print(all_tournaments_df)
print(all_tournaments_df[~all_tournaments_df["Tier"].isin(["D", "1"])])
print(all_tournaments_df[~all_tournaments_df["Tier"].isin(["D", "C", "B", "B+", "A", "A+"])])
print(set(all_tournaments_df["Tier"]))

# for tiers in [], get:
# tourney_slug, event_slug
# tournament_name, event_start_time, sets = get_all_info_for_tournament(tourney_slug, event_slug)

# save to a file {tourney_slug}.json
# with this:  json.dumps({"link": link, event: "event_slug", "tier": tier, "date": event_start_time, "name": tournament_name, "sets": sets})

# EXTRACTED_TOURNAMENTS_PATH


#https://docs.google.com/spreadsheets/d/1va7cwOc-fAH2fj6dmnE-4i_m2uYhGIkQvha44fExG-k/export?format=xlsx&gid=960683289#gid=960683289

#google_sheets_url = "https://docs.google.com/spreadsheets/d/1va7cwOc-fAH2fj6dmnE-4i_m2uYhGIkQvha44fExG-k/edit?gid=960683289#gid=960683289"




# google_sheets_url = "https://docs.google.com/spreadsheets/d/1va7cwOc-fAH2fj6dmnE-4i_m2uYhGIkQvha44fExG-k/edit?gid=639215028#gid=639215028"
# sheet_name = "TTS by Date (2024.2)"
# 

# download_google_sheet_as_excel(google_sheets_url, sheet_name, output_file)



# print(process_tournament_file(output_file))


from src.smash_data.puller import process_tournaments
TOURNAMENT_FOLDER_PATH = "/Users/deaxman/Downloads/all_smash_rankings/"
process_tournaments(google_sheets_url=None, sheet_name=None, tournament_folder_path=TOURNAMENT_FOLDER_PATH)





#player_name_to_tot_and_std_BEFORE_SWT = copy.copy(player_name_to_tot_and_std)

player_name_to_tot_and_std_sorted_AFTER_SWT = copy.copy(player_name_to_tot_and_std_sorted)



for player_name, [score, std_val] in player_name_to_tot_and_std_sorted_AFTER_SWT[:50]:
    if player_name in player_name_to_tot_and_std_BEFORE_SWT:
        print("{}\t{}\t{}\t{}\t{}".format(player_name, player_name_to_tot_and_std_BEFORE_SWT[player_name][0]/player_name_to_tot_and_std_BEFORE_SWT['MkLeo'][0], score/player_name_to_tot_and_std_sorted_AFTER_SWT[0][1][0], player_name_to_tot_and_std_BEFORE_SWT[player_name][1]/player_name_to_tot_and_std_BEFORE_SWT['MkLeo'][0], std_val/player_name_to_tot_and_std_sorted_AFTER_SWT[0][1][0]))




player_name_to_tot_and_std_sorted
player_name_to_tot_and_std
player_name_to_tot_and_std_sorted_AFTER_SWT











for wat in get_player_matchups(post_swt_post_quarantine, 'Tweek'):
    print('{} : {}-{}'.format(wat[0],wat[1][0], wat[1][1]))


for wat in get_player_matchups(post_swt_post_quarantine, 'Sparg0'):
    print('{} : {}-{}'.format(wat[0],wat[1][0], wat[1][1]))




import pandas as pd
#with open('/Users/deaxman/Downloads/matchup_chart.tsv')
matchup_chart = pd.read_csv('/Users/deaxman/Downloads/matchup_chart.tsv', sep='\t')
matchup_chart = matchup_chart.set_index(['Data used'])

matchup_chart = matchup_chart.drop(columns=["Unnamed: 1","Weighted Total","Weighted Score", "Mythra", "Pyra", 'Squirtle', 'Ivysaur', 'Charizard'])

matchup_chart = matchup_chart.drop(index=["Mythra", "Pyra", 'Squirtle', 'Ivysaur', 'Charizard'])


char_to_char_matchups = []
for p1 in matchup_chart.index:
    for p2 in matchup_chart.columns:
        logit_p1_beats_p2 = matchup_chart[p2][p1]
        try:
            logit_p1_beats_p2 = float(logit_p1_beats_p2)
            if np.isnan(logit_p1_beats_p2):
                print("{}: {} : {}".format(p1,p2,logit_p1_beats_p2))
                continue
        except ValueError:
            print("{}: {} : {}".format(p1,p2,logit_p1_beats_p2))
            continue
        percent_p1_beats_p2 = (1-(1/(1+np.exp(logit_p1_beats_p2/4))))
        char_to_char_matchups.append([p1, int(10*percent_p1_beats_p2), p2, 10-int(10*percent_p1_beats_p2)])



pair_df = pd.DataFrame(columns=['mean_matchup','mean_worst_5','number_good_matchups'])
#pair_df_all = pd.DataFrame(columns=matchup_chart.columns)
for i, p1 in enumerate(matchup_chart.index):
    for i2, p2 in enumerate(matchup_chart.index):
        if i != i2:
            m1 = matchup_chart.loc[p1] 
            m2 = matchup_chart.loc[p2]
            #m1 = m1[m1 != '-'].astype(float)
            #m2 = m2[m2 != '-'].astype(float)
            #pair_df_all.loc['{}_{}'.format(p1, p2)] = pd.concat([m1, m2], axis=1).min(axis=1)
            best_matchups = np.max([matchup_chart.loc[p1].to_numpy(), matchup_chart.loc[p2].to_numpy()], axis=0)
            best_matchups = best_matchups[best_matchups != '-'].astype(float)
            mean_matchup = np.mean(best_matchups)
            mean_worst_5 = np.mean(np.sort(best_matchups)[:5])
            number_good_matchups = np.sum(best_matchups>0)
            pair_df.loc['{}_{}'.format(p1, p2)] = pd.Series({'mean_matchup':mean_matchup, 'mean_worst_5':mean_worst_5, 'number_good_matchups':number_good_matchups})



1-(1/(1+np.exp(logit_p1_beats_p2/4)))

70/30   +4
65/35 (or 70/30)    +3
60/40 (or 70/30)    +2
55/45 (or 60/40)    +1
50/50   0


##########################################################################
##########################################################################
##########################################################################
##########################################################################

import matplotlib.pyplot as plt
from scipy.stats import norm
import matplotlib.colors as mcolors


fig, ax = plt.subplots(figsize=(9,6))
#plt.style.use('fivethirtyeight')

interesting_players_list=[
'MkLeo',
'Tweek',
'Sparg0',
'Tea',
'Light',
'Glutonny',
'Maister',
'Elegant',
'ESAM',
'Kola',
# 'Dabuz',
# 'Marss',
# 'Charliedaking',
# 'Lui$',
# 'Cosmos',
# 'VoiD',
# 'Goblin',
# 'Jakal',
# 'MuteAce',
# 'Chag',
# 'MVD',
# 'Fatality',
# 'LeoN',
# 'naitosharp',
# 'Larry Lurr',
# 'Tilde',
# 'BassMage',
# 'WaDi',
# 'Skyjay',
# 'Riddles'
]
colors = ['b', 'g', 'r', 'm', 'y', 'k', 'tab:orange', 'tab:cyan', '#00FF00', 'w']

for i, player_name in enumerate(interesting_players_list):
    x = np.arange(1, 6000, 0.01) # entire range of x, both in and out of spec
    # mean = 0, stddev = 1, since Z-transform was calculated
    y = norm.pdf(x, loc=player_name_to_tot_and_std[player_name][0], scale=player_name_to_tot_and_std[player_name][1])
    ax.plot(x,y, linewidth=3, label=player_name, color=colors[i])
    ax.fill_between(x,y,0, alpha=0.2, color='b')



ax.legend()

ax.set_xlim([1,6000])
ax.set_xlabel('Score for player')
ax.set_xlabel('Probability')
ax.set_yticklabels([])
ax.set_title('Score distribution for top players')

plt.savefig('/Users/deaxman/Downloads/top_player_scores.png', dpi=72, bbox_inches='tight')


plt.show()




get_player_matchups(games_after_quarantine,'Pandarian')


##########################################################################
##########################################################################
##########################################################################
##########################################################################





#VARIANCE COMPUTATION AND PRINTING AS IT TRAINS:



saved_weights = loss_eq.weights.detach().cpu().numpy()




loss_vects = []
ranking_score_list = []

for i in range(300000):
    opt.zero_grad()
    z, loss_vect = loss_eq()#new_loss(weights, p1_idx_arr, p2_idx_arr, s1_tensor, total_matches_tensor)
    if i == 0:
        loss_vect_old = loss_vect
    z.backward() # Calculate gradients
    opt.step()
    with torch.no_grad():
        _ = loss_eq.weights.clamp_(1.0, None)
    if i % 2000 == 0:
        print(i)
        print(z.data)
        sorted_improvements = (loss_vect_old - loss_vect).argsort()
        worst_regressions = sorted_improvements[:10]
        best_improvements = sorted_improvements[-10:]
        print('WORST')
        for idx in worst_regressions:
            p1_idx, p2_idx, s1, s2 = matchups[idx]
            print(player_list[p1_idx], player_list[p2_idx], s1, s2, loss_vect_old[idx], loss_vect[idx])
        print('BEST')
        for idx in best_improvements:
            p1_idx, p2_idx, s1, s2 = matchups[idx]
            print(player_list[p1_idx], player_list[p2_idx], s1, s2, loss_vect_old[idx], loss_vect[idx])
        ranking_scores = loss_eq.weights.detach().cpu().numpy()
        player_to_rating_dict = {player: rating for player, rating in zip(player_list, ranking_scores)}
        ranking_score_list.append(copy.copy(ranking_scores))
        display_player_rating(player_to_rating_dict, top=50)
        loss_vect_old = loss_vect
        loss_vects.append(loss_vect)





plt.figure(figsize=(14, 7))
plt.plot(-np.array(loss_vects).sum(axis=1))
plt.show()


x = np.linspace(0,1,10000)
y = torch.distributions.binomial.Binomial(torch.Tensor([3]*len(x)), torch.Tensor(x)).log_prob(torch.Tensor([0]*len(x)))

plt.figure(figsize=(14, 7))
plt.plot(x, y)
plt.show()



x = np.linspace(0,1,10000)
y = torch.distributions.binomial.Binomial(torch.Tensor([3]*len(x)), torch.Tensor(x)).log_prob(torch.Tensor([1]*len(x)))

plt.figure(figsize=(14, 7))
plt.plot(x, y)
plt.show()



def get_loss(test_weights, loss_eq):
    with torch.no_grad():
        test_weights=torch.Tensor(test_weights)
        expected_prob_p1_win_tensor = test_weights[loss_eq.p1_idx_arr]/(test_weights[loss_eq.p1_idx_arr] + test_weights[loss_eq.p2_idx_arr])
        loss_elem_vect = torch.distributions.binomial.Binomial(loss_eq.total_matches_tensor, expected_prob_p1_win_tensor).log_prob(loss_eq.s1_tensor)
        return -torch.sum(loss_elem_vect).detach().cpu().numpy()


def get_player_variance(player_name, loss_eq, ranking_scores):
    baseline_loss = get_loss(ranking_scores, loss_eq)
    num_increments = 100
    selected_player_idx = player_to_idx[player_name]
    factor_loss_list = []
    for factor in np.linspace(0.5, 1.5, num_increments):
        temp_weight = [weight_val if i != selected_player_idx else weight_val*factor for i, weight_val in enumerate(ranking_scores)]
        factor_loss_list.append([factor, np.abs(baseline_loss-get_loss(temp_weight, loss_eq))])
    upper_lim_list = [x[0] for x in factor_loss_list[int(num_increments/2):] if x[1] >= 0.5]
    if len(upper_lim_list) > 0:
        upper_lim = ranking_scores[selected_player_idx]*upper_lim_list[0]
    else:
        upper_lim = ranking_scores[selected_player_idx]*1.5
    lower_lim_list = [x[0] for x in factor_loss_list[:int(num_increments/2)][::-1] if x[1] >= 0.5]
    if len(lower_lim_list) > 0:
        lower_lim = ranking_scores[selected_player_idx]*lower_lim_list[0]
    else:
        lower_lim = ranking_scores[selected_player_idx]*1.5
    return [ranking_scores[selected_player_idx], lower_lim, upper_lim]




player_to_score_and_interval = {}
player_list_to_get_bounds_for = [player_name for player_name, _ in sorted(player_to_rating_dict.items(), key=lambda a: a[1], reverse=True)[:100]]
for i, player_name in enumerate(player_list_to_get_bounds_for):
    if i % 10 == 0:
        print(i, len(player_to_rating_dict))
    player_to_score_and_interval[player_name] = get_player_variance(player_name, loss_eq, ranking_scores)


for player_name, [score_val, lower_bound, upper_bound] in sorted(player_to_score_and_interval.items(), key=lambda a: a[1][0], reverse=True):
    print("{}\t{}\t{}\t{}".format(player_name, str(int(score_val)), str(int(lower_bound)), str(int(upper_bound))))



min_bound = np.min([upper_bound-lower_bound for player_name, [score_val, lower_bound, upper_bound] in sorted(player_to_score_and_interval.items(), key=lambda a: a[1][0], reverse=True)])
max_bound = np.max([upper_bound-lower_bound for player_name, [score_val, lower_bound, upper_bound] in sorted(player_to_score_and_interval.items(), key=lambda a: a[1][0], reverse=True)])

for player_name, [score_val, lower_bound, upper_bound] in sorted(player_to_score_and_interval.items(), key=lambda a: a[1][0], reverse=True):
    print("{}\t{}\t{}".format(player_name, str(int(score_val)), str(((upper_bound-lower_bound)-min_bound)/max_bound)))





#TOY DATA:

test_games=[('p1',100,'p2',10),('p3',10, 'p2', 1)]

elo if the above games happened once, note that P1 and P3 have different results:
p1: 1045.0951263030038
p2: 885.164199934489
p3: 1069.7406737625074

elo if the above games happened 1000 times, note that because elo is biased by play count we see that P1 and P3 have even more different results:
p1: 938.9474018706878
p2: 844.5914320750605
p3: 1216.4611660542528

my metric (same for 1000 times as for 1 time, just based on ratios):
p1: 625.9745
p2: 62.630276
p3: 625.9744

test_games=[('p3',10, 'p2', 1),('p1',100,'p2',10)]
game_list_unrolled_TEST = game_list_unroll(test_games)
player_to_rating_dict_overall_TEST = iterate_through_game_list_update_elo(game_list_unrolled_TEST, num_epochs=100)
display_player_rating(player_to_rating_dict_overall_TEST, top=50)


#Profiling
import cProfile, pstats
profiler = cProfile.Profile()
profiler.enable()
iterate_through_game_list_update_elo(random.sample(game_list_unrolled, len(game_list_unrolled)), num_epochs=1000)
profiler.disable()
stats = pstats.Stats(profiler).sort_stats('cumtime')
stats.print_stats()




#NEW TOURNAMENT!!!!!
new_tourn = {}
new_tourn_games = load_tournament_data(new_tourn)
games_after_quarantine_??? = games_after_quarantine_120821 + new_tourn_games
write_games('/Users/deaxman/Downloads/smash_after_quarantine_???.tsv', games_after_quarantine_???)
#games_after_quarantine_120821 = load_games('/Users/deaxman/Downloads/smash_after_quarantine_???.tsv')
GAMES=???

player_list = get_and_filter_player_list(GAMES, top=100000000)

player_to_matchup_list = defaultdict(lambda: defaultdict(lambda: np.array([0, 0])))
for game in GAMES:
    if len(game) == 4:
        p1, s1, p2, s2 = game
        player_to_matchup_list[p1][p2] += np.array([s1, s2])
        player_to_matchup_list[p2][p1] += np.array([s2, s1])
    else:
        print(game)

bad_player_set = set()
for p1, v in player_to_matchup_list.items():
    if sum([scores[0] for p2, scores in v.items()]) < 10 or sum([scores[1] for p2, scores in v.items()]) < 10:
        bad_player_set.add(p1)

player_list = [player for player in player_list if player not in bad_player_set]

matchups, player_to_idx = get_matchups(GAMES, player_list)

loss_eq = LossEq(player_list, matchups)
opt = torch.optim.Adam([loss_eq.weights], lr=0.1)
for i in range(50000):
    opt.zero_grad()
    z, loss_vect = loss_eq()
    z.backward() 
    opt.step()
    with torch.no_grad():
        _ = loss_eq.weights.clamp_(1.0, None)


ranking_scores_real = loss_eq.weights.detach().cpu().numpy()
player_to_rating_dict_real = {player: rating for player, rating in zip(player_list, ranking_scores_real)}


player_to_rating_dict_boot_list = []
for bootidx in range(100):
    print(bootidx)
    matchups_boot = random.choices(matchups, k=len(matchups))
    loss_eq = LossEq(player_list, matchups_boot)
    opt = torch.optim.Adam([loss_eq.weights], lr=0.1)
    for i in range(5000):
        opt.zero_grad()
        z, loss_vect = loss_eq()#new_loss(weights, p1_idx_arr, p2_idx_arr, s1_tensor, total_matches_tensor)
        z.backward() # Calculate gradients
        opt.step()
        with torch.no_grad():
            _ = loss_eq.weights.clamp_(1.0, None)
    ranking_scores = loss_eq.weights.detach().cpu().numpy()
    player_to_rating_dict = {player: rating for player, rating in zip(player_list, ranking_scores)}
    player_to_rating_dict_boot_list.append(player_to_rating_dict)


player_name_to_tot_and_std = {}
for player_name in player_to_rating_dict_boot_list[0]:
    player_name_to_tot_and_std[player_name] = [player_to_rating_dict_real[player_name], np.std([player_to_rating_dict_boot_list[boot_i][player_name] for boot_i in range(100)])]

player_name_to_tot_and_std_sorted = sorted(player_name_to_tot_and_std.items(), key=lambda a: a[1][0], reverse=True)
for player_name, [score, std_val] in player_name_to_tot_and_std_sorted:
    print("{}\t{}\t{}".format(player_name, score, std_val))







sudo yum -y install install python3-pip
python3 -m pip install pysmashgg
python3 -m pip install torch
python3 -m pip install numpy
python3 -m pip install boto3


import datetime


new_tournaments = [
'https://www.start.gg/tournament/let-s-make-moves-a-tristate-smash-ultimate-national-1/event/smash-ultimate-1v1/matches',
'https://www.start.gg/tournament/umebura-sp2/event/umebura-sp-singles/matches',
'https://www.start.gg/tournament/glitch-6/event/singles-1/matches',
'https://www.start.gg/tournament/genesis-6/event/smash-for-switch-singles/matches',
'https://www.start.gg/tournament/frostbite-2019/event/super-smash-bros-ultimate-singles/matches',
'https://www.start.gg/tournament/smash-ultimate-summit/event/ultimate-singles/matches',
'https://www.start.gg/tournament/collision-2019-super-smash-bros-ultimate-event/event/smash-ultimate-singles/matches',
'https://www.start.gg/tournament/sp3-umebura-sp3/event/umebura-sp-singles/matches',
'https://www.start.gg/tournament/2gg-prime-saga-1/event/ultimate-singles/matches',
'https://www.start.gg/tournament/pound-2019/event/ultimate-singles/matches',
'https://www.start.gg/tournament/japanmajor2019-umebura-japanmajor2019-1/event/singles/matches',
'https://www.start.gg/tournament/get-on-my-level-2019-canadian-fighting-game-championships-3/event/super-smash-bros-ultimate-singles/matches',
'https://www.start.gg/tournament/momocon-2019-1/event/smash-ultimate-singles/matches',
'https://www.start.gg/tournament/smash-n-splash-5/event/ultimate-singles/matches',
'https://www.start.gg/tournament/ceo-2019-fighting-game-championships/event/super-smash-bros-ultimate-singles/matches',
'https://www.start.gg/tournament/albion-4/event/smash-ultimate-singles/matches',
'https://www.start.gg/tournament/low-tier-city-7/event/smash-bros-ultimate-1v1/matches',
'https://www.start.gg/tournament/smash-factor-8/event/ultimate-singles/matches',
'https://www.start.gg/tournament/evo-2019/event/super-smash-bros-ultimate/matches',
'https://www.start.gg/tournament/super-smash-con-2019/event/ultimate-1v1-singles/matches',
'https://www.start.gg/tournament/sp4-umebura-sp4-2/event/singles/matches',
'https://www.start.gg/tournament/shine-2019/event/ultimate-singles',
'https://www.start.gg/tournament/2gg-switchfest-2019/event/ultimate-singles',
'https://www.start.gg/tournament/glitch-7-minus-world/event/singles/matches',
'https://www.start.gg/tournament/mainstage/event/ultimate-singles',
'https://www.start.gg/tournament/sp5-umebura-sp5/event/singles',
'https://www.start.gg/tournament/ultimate-fighting-arena-2019/event/super-smash-bros-ultimate-single-1vs1',
'https://www.start.gg/tournament/the-big-house-9/event/ultimate-singles',
'https://www.start.gg/tournament/thunder-smash-3-clash-of-the-pandas/event/thunder-smash-3-panda-storm/overview',
'https://www.start.gg/tournament/sp6-umeburasp6/event/singles/matches',
'https://www.start.gg/tournament/smash-ultimate-summit-2/event/smash-ultimate-summit/matches',
'https://www.start.gg/tournament/syndicate-2019/event/singles',
'https://www.start.gg/tournament/sp7-umeburasp7/event/singles',
'https://www.start.gg/tournament/dreamhack-atlanta-2019/event/smash-ultimate-1v1',
'https://www.start.gg/tournament/2gg-kongo-saga/event/ultimate-singles',
'https://www.start.gg/tournament/let-s-make-big-moves-a-tristate-smash-ultimate-national/event/smash-ultimate-1v1',
'https://www.start.gg/tournament/egs-cup-3/event/special-1on1-ultimate-singles',
'https://www.start.gg/tournament/glitch-8-missingno-2/event/singles',
'https://www.start.gg/tournament/genesis-7-1/event/ultimate-singles',
'https://www.start.gg/tournament/evo-japan-2020/event/evo-japan-2020-super-smash-bros-ultimate',
'https://www.start.gg/tournament/frostbite-2020/event/super-smash-bros-ultimate-1v1-singles',
'https://www.start.gg/tournament/3-kagaribi-3/event/singles/matches',
'https://www.start.gg/tournament/4-kagaribi-4-1/event/singles/matches',
'https://www.start.gg/tournament/ultimate-wanted-3/event/singles-1vs1-saturday-sunday-2',
'https://www.start.gg/tournament/smash-ultimate-summit-3/event/ultimate-singles/matches',
'https://www.start.gg/tournament/temple-herm-s-edition/event/ultimate-singles',
'https://www.start.gg/tournament/riptide-3/event/ultimate-singles/matches',
'https://www.start.gg/tournament/glitch-8-5-konami-code/event/ultimate-singles/matches',
'https://www.start.gg/tournament/low-tide-city-2021/event/smash-bros-ultimate-1v1/matches',
'https://www.start.gg/tournament/8-11/event/singles',
'https://www.start.gg/tournament/super-smash-con-fall-fest/event/ultimate-1v1-singles/matches',
'https://www.start.gg/tournament/top-6-maesumatop-6-1on1/event/singles-tournament/matches',
'https://www.start.gg/tournament/port-priority-6/event/ultimate-singles/matches',
'https://www.start.gg/tournament/5-kagaribi-5-1/event/singles-1/matches',
'https://www.start.gg/tournament/mainstage-2021/event/ultimate-singles/matches',
'https://www.start.gg/tournament/vca-vienna-challengers-arena-2021/event/super-smash-bros-ultimate-singles',
'https://www.start.gg/tournament/ceo-2021-fighting-game-championships/event/super-smash-bros-ultimate',
'https://www.start.gg/tournament/the-smash-world-tour-championships/event/ultimate-championships/matches',
'https://www.start.gg/tournament/let-s-make-big-moves-2022/event/ultimate-singles',
'https://www.start.gg/tournament/6-kagaribi-6/event/singles/matches',
'https://www.start.gg/tournament/glitch-infinite-2/event/ultimate-singles-starts-saturday',
'https://www.start.gg/tournament/smash-ultimate-summit-4/event/ultimate-singles',
'https://www.start.gg/tournament/collision-2022/event/ultimate-singles',
'https://www.start.gg/tournament/delfino-maza-reta-2022/event/ultimate-singles',
'https://www.start.gg/tournament/genesis-8/event/ultimate-singles',
'https://www.start.gg/tournament/pound-2022/event/ultimate-singles-2',
'https://www.start.gg/tournament/low-tide-city-2022/event/smash-bros-ultimate-1v1',
'https://www.start.gg/tournament/top-7-maesumatop-7/event/singles-tournament/matches',
'https://www.start.gg/tournament/7-kagaribi-7/event/singles',
'https://www.start.gg/tournament/momocon-2022-1/event/smash-ultimate-singles',
'https://www.start.gg/tournament/battle-of-bc-4-2/event/ultimate-singles-bracket',
'https://www.start.gg/tournament/top-8-maesumatop-8/event/singles-tournament',
'https://www.start.gg/tournament/the-gimvitational-1/event/ultimate-singles',
'https://www.start.gg/tournament/crown-2/event/ultimate-singles',
'https://www.start.gg/tournament/e-caribana-presented-by-andros/event/ecaribana-invitational-presented-by-andros',
'https://www.start.gg/tournament/ceo-2022-fighting-game-championships/event/super-smash-bros-ultimate-1',
'https://www.start.gg/tournament/95-kings-of-fields-2/event/tournoi-ssbu-kof95-2',
'https://www.start.gg/tournament/get-on-my-level-2022-canadian-fighting-game-championships-3/event/super-smash-bros-ultimate-singles',
'https://www.start.gg/tournament/colossel-2022/event/ultimate-singles',
'https://www.start.gg/tournament/double-down-2022/event/ultimate-singles-starts-saturday',
'https://www.start.gg/tournament/smash-factor-9-1/event/ultimate-singles',
'https://www.start.gg/tournament/8-kagaribi-8-7/event/singles/overview',
'https://www.start.gg/tournament/super-smash-con-2022/event/ultimate-1v1-singles',
'https://www.start.gg/tournament/rise-n-grind/event/super-smash-bros-ultimate-singles-1',
'https://www.start.gg/tournament/top-9-maesumatop-9/event/singles-tournament',
'https://www.start.gg/tournament/ultimate-wanted-4-powered-by-predator/event/singles-1vs1-saturday-sunday/overview',
'https://www.start.gg/tournament/smash-ultimate-summit-5-presented-by-coinbase/event/ultimate-singles',
'https://www.start.gg/tournament/vca-vienna-challengers-arena-2022/event/super-smash-bros-ultimate-singles/matches',
'https://www.start.gg/tournament/the-big-house-10/event/ultimate-singles',
'https://www.start.gg/tournament/top-10-maesumatop-10/events/singles-tournament/matches',
'https://www.start.gg/tournament/l-odyss-e/event/singles/matches',
'https://www.start.gg/tournament/ludwig-smash-invitational/events/ultimate-singles-main-event/matches']



import hashlib
uniq_tourneyset_str = ",".join(sorted(["/".join([t.split("/")[4], t.split("/")[6]]) for t in new_tournaments))
uniq_tourneyset_key = hashlib.sha256(uniq_tourneyset_str.encode()).hexdigest()



2048


new_tournaments = ['https://www.start.gg/tournament/ludwig-smash-invitational/event/ultimate-singles-main-event/matches']

new_tournaments = ['https://www.start.gg/tournament/let-s-make-moves-miami/event/ultimate-singles/matches']
game_dict = update_tournament_cache(new_tournaments)



https://www.start.gg/tournament/let-s-make-moves-miami/event/ultimate-singles/matches




game_dict_ALL = load_json(Path.home()/'game_dict.json')


convert_game_score_to_winlose_set()


selected_tournament_urls = get_tournaments_from_date_range(tournament_to_date_dict, start_date=datetime.datetime(2017, 1, 1, 0, 0), end_date=datetime.datetime(2022, 10, 19, 0, 0))
all_games = get_game_list_from_list_of_tournaments(game_dict, selected_tournament_urls)

player_list = get_and_filter_player_list(all_games, top=None, min_win_loss=10)
matchups, player_to_idx = get_matchups(all_games, player_list)



matchups_filtered = [matchup for matchup in matchups if matchup[2]+matchup[3] > 13]
sorted_by_worst = sorted(matchups_filtered, key = lambda a: (a[2]+1)/(a[3]+1) if (a[3]+1)<=(a[2]+1) else (a[3]+1)/(a[2]+1), reverse=True)



wat = [[player_list[matchup[0]], player_list[matchup[1]], matchup[2], matchup[3]] for matchup in sorted_by_worst]

wat

get_player_matchups(, "Tweek")


for k in game_dict_ALL:
    print(k, len(game_dict_ALL[k]))





aws s3 cp s3://smash-ranking/data/game_dict_10232022.json ~/game_dict.json
aws s3 cp s3://smash-ranking/data/tournament_to_date_dict_10232022.json ~/tournament_to_date_dict.json

rankings_dict_ALL, selected_tournament_urls_ALL, config_ALL = get_rankings(start_date=datetime.datetime(2022, 6, 14, 0, 0), end_date=datetime.datetime(2022, 10, 25, 0, 0), top_player_number=None, min_win_loss=1, rankings_to_run=("elo_games", "elo_sets", "h2h_ratio_games", "h2h_ratio_sets"))








tournament_to_date_dict = load_json(ALL_TOURNAMENTS_DATES_FILE)
get_tournaments_from_date_range(tournament_to_date_dict, start_date=datetime.datetime(2022, 1, 1, 0, 0), end_date=datetime.datetime(2022, 10, 19, 0, 0))


rankings_dict, selected_tournament_urls, config = get_rankings(start_date=datetime.datetime(2022, 1, 1, 0, 0), end_date=datetime.datetime(2022, 10, 19, 0, 0), top_player_number=None, min_win_loss=10, rankings_to_run=("elo_games", "elo_sets", "h2h_ratio_games", "h2h_ratio_sets"))



rankings_dict, selected_tournament_urls, config = get_rankings(start_date=datetime.datetime(2022, 1, 1, 0, 0), end_date=datetime.datetime(2022, 10, 19, 0, 0), top_player_number=None, min_win_loss=10, rankings_to_run=("h2h_ratio_games", "h2h_ratio_sets"))




rankings_dict_ALL, selected_tournament_urls_ALL, config_ALL = get_rankings(start_date=datetime.datetime(2022, 1, 1, 0, 0), end_date=datetime.datetime(2022, 10, 19, 0, 0), top_player_number=None, min_win_loss=1, rankings_to_run=("elo_games", "elo_sets", "h2h_ratio_games"))






player_to_rating_dict_real_sorted = sorted(rankings_dict_ALL["elo_sets"], key=lambda a: a[1], reverse=True)

count = 0
for p, s in player_to_rating_dict_real_sorted:
    if count > 50:
        break
    print(p, s)
    count +=1


count = 0
for p, m, v in rankings_dict["h2h_ratio_sets"]:
    print(p, m, v)
    count +=1
    if count > 50:
        break



class LossEq(nn.Module):
    def __init__(self, player_list, matchups, player_to_rating_dict_overall=None):
        super().__init__()
        if player_to_rating_dict_overall is not None:
            rating_list = np.array([float(player_to_rating_dict_overall[player]) if player in player_to_rating_dict_overall else 1000.0  for player in player_list])
            rating_list_normalized = ((rating_list - np.min(rating_list))/np.mean(rating_list))*3+1
            rating_list_normalized_exp = np.power(np.e, rating_list_normalized)
            self.weights = nn.Parameter(torch.Tensor(rating_list_normalized_exp))
        else:
            self.weights = nn.Parameter(torch.Tensor([400.0 for _ in range(len(player_list))]))
        #self.weights = nn.Parameter(torch.Tensor([100.0 for _ in range(num_players)]))
        s1_arr = np.array([float(matchup[2]) for matchup in matchups])
        s2_arr = np.array([float(matchup[3]) for matchup in matchups])
        total_matches_arr = s1_arr + s2_arr
        self.p1_idx_arr = np.array([matchup[0] for matchup in matchups])
        self.p2_idx_arr = np.array([matchup[1] for matchup in matchups])
        self.s1_tensor = torch.tensor(s1_arr)
        self.total_matches_tensor = torch.tensor(total_matches_arr)
        #self.loss = 0
        # for matchup in matchups:
        #     p1_rating = self.weights[matchup[0]]
        #     p2_rating = self.weights[matchup[1]]
        #     p1_estimated_winning_prob = p1_rating/(p1_rating + p2_rating)
        #     self.loss += torch.distributions.binomial.Binomial(float(matchup[2]) + float(matchup[3]), p1_estimated_winning_prob).log_prob(torch.tensor([float(matchup[2])]))
    def forward(self):
        expected_prob_p1_win_tensor = torch.exp(self.weights[self.p1_idx_arr]/(self.weights[self.p1_idx_arr] + self.weights[self.p2_idx_arr]))
        loss_elem_vect = torch.distributions.binomial.Binomial(self.total_matches_tensor, expected_prob_p1_win_tensor).log_prob(self.s1_tensor)
        loss_val = -torch.sum(loss_elem_vect)
        return loss_val, loss_elem_vect.detach().cpu().numpy()



tournament_to_date_dict = load_json(ALL_TOURNAMENTS_DATES_FILE)
game_dict = load_json(ALL_TOURNAMENTS_GAMES_FILE)
selected_tournament_urls = get_tournaments_from_date_range(tournament_to_date_dict, start_date=datetime.datetime(2022, 1, 1, 0, 0), end_date=datetime.datetime(2022, 10, 19, 0, 0))
all_games = get_game_list_from_list_of_tournaments(game_dict, selected_tournament_urls)
player_list = get_and_filter_player_list(all_games, top=None, min_win_loss=10)
matchups, player_to_idx = get_matchups(all_games, player_list)



iters=50000
loss_eq = LossEq(player_list, matchups)
opt = torch.optim.Adam([loss_eq.weights], lr=0.1)
all_losses = []
for i in range(iters):
    opt.zero_grad()
    z, loss_vect = loss_eq()
    z.backward()
    opt.step()
    with torch.no_grad():
        _ = loss_eq.weights.clamp_(1.0, None)
    all_losses.append(float(z))



import matplotlib.pyplot as plt
plt.plot(range(len(all_losses)), all_losses)



from collections import defaultdict

game_dict_ALL = load_json(ALL_TOURNAMENTS_GAMES_FILE)
game_dict_new = defaultdict(list)
for t, games in game_dict_ALL.items():
    count = 0
    for game in games:
        if game[1] < 0 or game[3] < 0:
            count += 1
        else:
            game_dict_new[t].append(game)
    print(t, count)

game_dict_new


wat = ["https://www.start.gg/tournament/ceo-2019-fighting-game-championships/event/super-smash-bros-ultimate-singles/matches",
"https://www.start.gg/tournament/evo-2019/event/super-smash-bros-ultimate/matches",
"https://www.start.gg/tournament/2gg-kongo-saga/event/ultimate-singles",
"https://www.start.gg/tournament/evo-japan-2020/event/evo-japan-2020-super-smash-bros-ultimate",
"https://www.start.gg/tournament/mainstage-2021/event/ultimate-singles/matches",
"https://www.start.gg/tournament/genesis-8/event/ultimate-singles"]

for t in wat:
    print(t, len(game_dict_new[t]), len(game_dict_ALL[t]))


game_dict_ALL["https://www.start.gg/tournament/ceo-2019-fighting-game-championships/event/super-smash-bros-ultimate-singles/matches"]
https://www.start.gg/tournament/evo-2019/event/super-smash-bros-ultimate/matches

bad_t = set()
for t, games in game_dict_ALL.items():
    for game in games:
        if game[1] < 0 or game[3] < 0:
            bad_t.add(t)
            print(game)


print(bad_t)





for game in game_dict_ALL['https://www.start.gg/tournament/evo-2019/event/super-smash-bros-ultimate/matches']:
    if not (game[1] < 0 or game[3] < 0):
        print(game)


all_rankings = get_rankings(start_date=None, end_date=None, top_player_number=None, min_win_loss=0, rankings_to_run=("elo_games", "elo_sets", "h2h_ratio_games", "h2h_ratio_sets"))



INFO:root:https://www.start.gg/tournament/2gg-prime-saga-1/event/ultimate-singles/matches
INFO:root:0
INFO:root:1
INFO:root:2
INFO:root:3
INFO:root:4
INFO:root:5
INFO:root:6
INFO:root:7
INFO:root:8
INFO:root:9
INFO:root:10
INFO:root:11
INFO:root:12
INFO:root:13
INFO:root:14
INFO:root:15
INFO:root:16
INFO:root:17
INFO:root:18

INFO:root:https://www.start.gg/tournament/smash-n-splash-5/event/ultimate-singles/matches
INFO:root:0
INFO:root:1
INFO:root:https://www.start.gg/tournament/ceo-2019-fighting-game-championships/event/super-smash-bros-ultimate-singles/matches
INFO:root:0
INFO:root:1
INFO:root:2

INFO:root:https://www.start.gg/tournament/glitch-smash-7/event/ultimate-singles
INFO:root:0
INFO:root:1
INFO:root:2
INFO:root:3

INFO:root:https://www.start.gg/tournament/evo-japan-2020/event/evo-japan-2020-super-smash-bros-ultimate
INFO:root:0
INFO:root:1
INFO:root:2
INFO:root:3


INFO:root:https://www.start.gg/tournament/frostbite-2020/event/super-smash-bros-ultimate-1v1-singles
INFO:root:0


INFO:root:https://www.start.gg/tournament/4-kagaribi-4-1/event/singles/matches
INFO:root:0
INFO:root:1
INFO:root:2
INFO:root:3
INFO:root:4
INFO:root:5
INFO:root:6


INFO:root:https://www.start.gg/tournament/ceo-2021-fighting-game-championships/event/super-smash-bros-ultimate
INFO:root:0
INFO:root:1
INFO:root:2
INFO:root:3
INFO:root:4
INFO:root:5


INFO:root:https://www.start.gg/tournament/6-kagaribi-6/event/singles/matches
INFO:root:0

INFO:root:https://www.start.gg/tournament/let-s-make-big-moves-2022/event/ultimate-singles
INFO:root:0
INFO:root:1
INFO:root:2
INFO:root:3
INFO:root:4
INFO:root:5




remove that glitch from the tournament times as well!!!!!!!!!!!
jq 'del(.["https://www.start.gg/tournament/glitch-smash-7/event/ultimate-singles"])' game_dict.json > ~/game_dict_new.json



rerun_these=['https://www.start.gg/tournament/2gg-prime-saga-1/event/ultimate-singles/matches',
'https://www.start.gg/tournament/smash-n-splash-5/event/ultimate-singles/matches',
'https://www.start.gg/tournament/ceo-2019-fighting-game-championships/event/super-smash-bros-ultimate-singles/matches',
'https://www.start.gg/tournament/glitch-7-minus-world/event/singles/matches',
'https://www.start.gg/tournament/evo-japan-2020/event/evo-japan-2020-super-smash-bros-ultimate',
'https://www.start.gg/tournament/frostbite-2020/event/super-smash-bros-ultimate-1v1-singles',
'https://www.start.gg/tournament/4-kagaribi-4-1/event/singles/matches',
'https://www.start.gg/tournament/ceo-2021-fighting-game-championships/event/super-smash-bros-ultimate',
'https://www.start.gg/tournament/let-s-make-big-moves-2022/event/ultimate-singles',
'https://www.start.gg/tournament/6-kagaribi-6/event/singles/matches']

game_dict2 = update_tournament_cache(rerun_these)

ceo-2019-fighting-game-championships
evo-japan-2020/


final_rerun = ['https://www.start.gg/tournament/ceo-2019-fighting-game-championships/event/super-smash-bros-ultimate-singles/matches',
'https://www.start.gg/tournament/evo-japan-2020/event/evo-japan-2020-super-smash-bros-ultimate']

game_dict4 = update_tournament_cache(final_rerun)




tourn_101622_update = ['https://www.start.gg/tournament/top-10-maesumatop-10/events/singles-tournament/matches',
'https://www.start.gg/tournament/l-odyss-e/event/singles/matches']


game_dict5 = update_tournament_cache(tourn_101622_update)


fix_maesuma = ['https://www.start.gg/tournament/top-7-maesumatop-7/event/singles-tournament/matches']

game_dict_fix_maesuma = update_tournament_cache(fix_maesuma)


aws s3 cp ~/game_dict.json s3://smash-ranking/data/game_dict_10232022.json
aws s3 cp ~/tournament_to_date_dict.json s3://smash-ranking/data/tournament_to_date_dict_10232022.json




aws s3 cp s3://smash-ranking/data/game_dict_10162022_fix_maesuma_dropnegative.json ~/game_dict.json
aws s3 cp s3://smash-ranking/data/tournament_to_date_dict_10162022_fix_maesuma.json ~/tournament_to_date_dict.json








import copy

gd = copy.deepcopy(game_dict)

gd.update(game_dict2)

gd.update(game_dict3)


write_json(gd, '/home/ec2-user/newest_game_dict.json')


jq 'del(.["https://www.start.gg/tournament/glitch-smash-7/event/ultimate-singles"])' /home/ec2-user/newest_game_dict.json > ~/final_game_dict.json

jq 'del(.["https://www.start.gg/tournament/glitch-smash-7/event/ultimate-singles"])' /home/ec2-user/tournament_to_date_dict_new.json > ~/final_tournament_to_date_dict.json

mv ~/game_dict.json ~/game_dict_OLD.json
mv ~/tournament_to_date_dict.json ~/tournament_to_date_dict_OLD.json
cp ~/final_game_dict.json ~/game_dict.json
cp ~/final_tournament_to_date_dict.json ~/tournament_to_date_dict.json


cp ~/game_dict.json ~/game_dict_to_tbh10.json
cp ~/tournament_to_date_dict.json ~/tournament_to_date_dict_to_tbh10.json


rm ~/tournament_to_date_dict.json
rm ~/game_dict.json
cp ~/game_dict_to_tbh10.json ~/game_dict.json
cp ~/tournament_to_date_dict_to_tbh10.json ~/tournament_to_date_dict.json





for k in game_dict3:
    print(k)
    print(len(game_dict3[k]))



import time

for tournament in new_tournaments:
    tourn_name = tournament.split("/")[4]
    bracket = tournament.split("/")[6]
    print(tourn_name, bracket)
    if "evo-2019" == tourn_name:
        1564740000
    if "sp6-umeburasp6" == tourn_name:
        1571652000
    tournament_info = SMASH.tournament_show_with_brackets(tourn_name, bracket)
    time.sleep(.75)














#TODO:
make list of all configs in liquidipedia
change code to update after every tourney??
make code to read and write cache stuff to s3
put the list of all tournaments in dynamodb??
make pulling from DDB code


dockerize everything


run all tourney pull






smash.tournament_show_sets("evo-2019", "ultimate-singles", 1)


smash.tournament_show_sets("sp6-umeburasp6", "singles", 1)
















import boto3
import os
import requests
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('WalletRecoverInfo')





table.put_item(
    Item={
        "included_tournaments"
        "config":
    }
)






def write_PIN_to_ddb(PIN):
    import boto3
    import requests
    import time
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('WalletRecoverRunMetadata')
    response = {}
    while 'ResponseMetadata' not in response or response['ResponseMetadata']['HTTPStatusCode'] != 200:
        response = table.put_item(
            Item={
                'MetadataField': 'PIN',
                'PIN_VALUE': str(PIN)
            }
        )
        time.sleep(0.5)
    table = dynamodb.Table('WalletRecoverInfo')
    print('FOUND PIN: {}'.format(str(PIN)))
    print('Writing PIN to DDB')
    response = {}
    while 'ResponseMetadata' not in response or response['ResponseMetadata']['HTTPStatusCode'] != 200:
        response = table.update_item(
            Key={
                    'SearchRange': btcrpass.get_search_range(btcrpass.args.tokenlist),
                    'ClusterID': btcrpass.get_uniq_instance_id()
            },
            UpdateExpression="set PIN = :r",
            ExpressionAttributeValues={
                ':r': str(PIN),
            },
            ReturnValues="UPDATED_NEW"
        )
        time.sleep(0.5)



def write_progress(rate, complete, table):
    response = {}
    count_loops = 0
    while True:
        response = table.put_item(
           Item={
                'ClusterID': str(requests.get('http://169.254.169.254/latest/meta-data/instance-id').text),
                'Rate': str(rate),
                'Complete': str(complete)
            }
        )
        if 'ResponseMetadata' not in response or response['ResponseMetadata']['HTTPStatusCode'] != 200:
            if count_loops > 5:
                print('ERROR writing progress to DDB:  '+ str(response['ResponseMetadata']))
                break
            else:
                count_loops += 1
                time.sleep(0.5)
        else:
            break


import boto3
import os
import requests
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('WalletRecoverInfo')




dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('WalletRecoverRunMetadata')
    response = {}
    while 'Item' not in response or 'PasswordValue' not in response['Item']:
        response = table.get_item(Key={'MetadataField': 'Password'})
        time.sleep(0.5)
    password = response['Item']['PasswordValue']









"https://www.start.gg/tournament/ludwig-smash-invitational/event/ultimate-singles-main-event/matches"



tournament_to_date_dict_NEW = load_json(ALL_TOURNAMENTS_DATES_FILE)
game_dict_NEW = load_json(ALL_TOURNAMENTS_GAMES_FILE)


new_tournaments = ['https://www.start.gg/tournament/ludwig-smash-invitational/events/ultimate-singles-main-event/brackets/1192747/1844219/matches',
'https://www.start.gg/tournament/ludwig-smash-invitational/events/ultimate-singles-main-event/brackets/1192747/1893382/matches',
'https://www.start.gg/tournament/ludwig-smash-invitational/events/ultimate-singles-main-event/brackets/1233356/1898100/matches']

for t in new_tournaments:
	game_dict_NEW.pop(t)
	tournament_to_date_dict_NEW.pop(t)


write_json(tournament_to_date_dict_NEW, ALL_TOURNAMENTS_DATES_FILE)
write_json(game_dict_NEW, ALL_TOURNAMENTS_GAMES_FILE)


new_tournaments = ['https://www.start.gg/tournament/ludwig-smash-invitational/event/ultimate-singles-main-event/matches']

game_dict4 = update_tournament_cache(new_tournaments)


wat = [['Zomba', 3, 'Asimo', 0], ['Cosmos', 3, 'zackray', 2], ['Dabuz', 3, 'Marss', 0], ['Glutonny', 3, 'goblin deez', 0], ['Tea', 2, 'Kurama', 3], ['あcola', 3, 'Quandale', 1], ['Marss', 1, 'Tea', 3], ['Asimo', 3, 'Quandale Dinglelingleton', 0], ['Dabuz', 3, 'Kurama', 1], ['MkLeo', 3, 'Cosmos', 0], ['Glutonny', 0, 'Sonix', 3], ['Quandale Dinglelingleton', 3, 'goblin deez', 1], ['MkLeo', 0, 'Dabuz', 3], ['Sonix', 3, 'Tea', 2], ['Dabuz', 2, 'あcola', 3], ['Quandale Dinglelingleton', 3, 'zackray', 0], ['Scend', 0, 'Asimo', 3], ['Cosmos', 3, 'Chag', 0], ['Glutonny', 0, 'Kurama', 3], ['Big D', 3, 'Jakal', 1], ['Light', 2, 'Onin', 3], ['Kola', 3, 'Riddles', 1], ['Maister', 0, 'Sparg0', 3], ['Big D', 3, 'Riddles', 0], ['Tweek', 3, 'Myran', 0], ['Jakal', 3, 'KEN', 2], ['MFA', 0, 'Light', 3], ['Onin', 3, 'Sisqui', 0], ['Tweek', 0, 'Kola', 3], ['Sisqui', 3, 'Lima', 2], ['Jakal', 3, 'Myran', 0], ['Light', 3, 'MuteAce', 2], ['Light', 0, 'Big D', 3], ['Riddles', 3, 'Lima', 1], ['Sparg0', 3, 'Jakal', 2], ['Tweek', 3, 'KEN', 1], ['MkLeo', 3, 'あcola', 0], ['Tweek', 3, 'Maister', 1], ['Cosmos', 1, 'Dabuz', 3], ['Quandale Dinglelingleton', 1, 'Glutonny', 3], ['Asimo', 3, 'Tea', 1], ['Kurama', 1, 'MkLeo', 3], ['Kurama', 1, 'あcola', 3], ['MkLeo', 3, 'あcola', 0], ['Jakal', 1, 'Riddles', 3], ['Sisqui', 2, 'Light', 3], ['Sparg0', 2, 'あcola', 3], ['Shuton', 1, 'Kurama', 3], ['あcola', 0, 'MkLeo', 3], ['Shuton', 0, 'Sparg0', 3], ['あcola', 3, 'Onin', 0], ['Glutonny', 3, 'Asimo', 1], ['Sisqui', 3, 'Tweek', 1], ['Tea', 3, 'Cosmos', 0], ['Kola', 1, 'Onin', 3], ['Sonix', 0, 'Sparg0', 3], ['Shuton', 3, 'Big D', 0], ['Kola', 1, 'Kurama', 3], ['Riddles', 2, 'あcola', 3], ['MkLeo', 3, 'Sonix', 0], ['Riddles', 3, 'Maister', 2], ['Sonix', 3, 'Glutonny', 1], ['Riddles', 1, 'Sparg0', 3], ['Kola', 3, 'Zomba', 2], ['Big D', 0, 'Onin', 3], ['Glutonny', 3, 'Tweek', 0], ['Dabuz', 0, 'Sparg0', 3], ['Zomba', 3, 'Light', 2], ['Asimo', 0, 'Onin', 3], ['Shuton', 3, 'Glutonny', 1], ['Big D', 3, 'Tweek', 1], ['Kola', 3, 'Dabuz', 0], ['Sparg0', 2, 'Kurama', 3], ['Zomba', 1, 'Riddles', 3], ['あcola', 3, 'Light', 2], ['MkLeo', 3, 'Asimo', 0], ['Sonix', 3, 'Onin', 2], ['Maister', 3, 'Sisqui', 1]]



from collections import defaultdict

wat2 = defaultdict(int)

for g in wat:
	wat2[tuple(g)] += 1


[g for g, v in wat2.items() if v > 1]


game_dict_NEW = load_json(ALL_TOURNAMENTS_GAMES_FILE)

game_dict_NEW['https://www.start.gg/tournament/ludwig-smash-invitational/event/ultimate-singles-main-event/matches'] = wat
write_json(game_dict_NEW, ALL_TOURNAMENTS_GAMES_FILE)


n = 18
k = 8
binom_integ(n, k, 4, 3)/(binom_integ(n, k, 4, 4) + binom_integ(n, k, 4, 3) + binom_integ(n, k, 4, 2) + binom_integ(n, k, 4, 1) + binom_integ(n, k, 1, 0))
binom_integ(n, k, 4, 1)/(binom_integ(n, k, 4, 4) + binom_integ(n, k, 4, 3) + binom_integ(n, k, 4, 2) + binom_integ(n, k, 4, 1) + binom_integ(n, k, 1, 0))


import numpy as np


interest_rates_voo_2011_2022 = np.array([2, 16, 32.3, 13.6, 1.3, 12, 21.7, -4.47, 31.47, 18.4, 28.6, -18.15])
interest_rates_voo_2011_2022_IUL_CAPPED = np.array([12 if i>12 else (1 if i<1 else i) for i in interest_rates_voo_2011_2022])
np.prod((interest_rates_voo_2011_2022/100)+1)
np.prod((interest_rates_voo_2011_2022_IUL_CAPPED/100)+1)







sudo yum -y install aws-cli
aws s3 cp s3://smash-ranking/data/game_dict_10292022.json ~/game_dict.json
aws s3 cp s3://smash-ranking/data/tournament_to_date_dict_10292022.json ~/tournament_to_date_dict.json

python3 -m pip install pysmashgg
python3 -m pip install numpy
python3 -m pip install torch
python3 -m pip install tqdm
python3 -m pip install matplotlib



sudo yum -y install aws-cli
sudo yum -y install install python3-pip
python3 -m pip install pysmashgg
python3 -m pip install torch
python3 -m pip install numpy
python3 -m pip install boto3
python3 -m pip install tqdm
python3 -m pip install matplotlib
python3 -m pip install pandas


python3
rankings_dict_elo_games, selected_tournament_urls_elo_games, config_elo_games = get_rankings(start_date=datetime.datetime(2022, 6, 14, 0, 0), end_date=datetime.datetime(2022, 10, 28, 0, 0), top_player_number=None, min_win_loss=1, rankings_to_run=("elo_games"))


rankings_dict_elo_sets, selected_tournament_urls_elo_sets, config_elo_sets = get_rankings(start_date=datetime.datetime(2022, 6, 14, 0, 0), end_date=datetime.datetime(2022, 10, 28, 0, 0), top_player_number=None, min_win_loss=1, rankings_to_run=("elo_sets"))


rankings_dict_h2h_ratio_games, selected_tournament_urls_h2h_ratio_games, config_h2h_ratio_games = get_rankings(start_date=datetime.datetime(2022, 6, 14, 0, 0), end_date=datetime.datetime(2022, 10, 28, 0, 0), top_player_number=None, min_win_loss=1, rankings_to_run=("h2h_ratio_games"))


rankings_dict_h2h_ratio_sets, selected_tournament_urls_h2h_ratio_sets, config_h2h_ratio_sets = get_rankings(start_date=datetime.datetime(2022, 6, 14, 0, 0), end_date=datetime.datetime(2022, 10, 28, 0, 0), top_player_number=None, min_win_loss=1, rankings_to_run=("h2h_ratio_sets"))




python3
rankings_dict_elo_sets, selected_tournament_urls_elo_sets, config_elo_sets = get_rankings(start_date=datetime.datetime(2022, 1, 1, 0, 0), end_date=datetime.datetime(2022, 10, 28, 0, 0), top_player_number=None, min_win_loss=1, rankings_to_run=("elo_games"))




player_to_rating_dict_real_sorted = sorted(rankings_dict_elo_sets["elo_games"], key=lambda a: a[1], reverse=True)

count = 0
for p, s in player_to_rating_dict_real_sorted:
    if count > 100:
        break
    print(p, s)
    count +=1



import boto3
from datetime import datetime
import uuid
from pathlib import Path
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('SmashRankingData')
s3 = boto3.resource('s3')


def get_recent_artifacts():
    tournament_to_date_dict_file = Path().home()/'tournament_to_date_dict.json'
    game_dict_file = Path().home()/'game_dict.json'
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
    datestamp = str(datetime.now()).replace(" ", "-")
    checksum = str(uuid.uuid4())
    tournament_to_date_dict_s3uri = f"data/{datestamp}/tournament_to_date_dict_{checksum}.json"
    game_dict_s3uri = f"data/{datestamp}/game_dict_{checksum}.json"
    s3.Bucket('smash-ranking').upload_file(str(Path().home()/'tournament_to_date_dict.json'), tournament_to_date_dict_s3uri)
    s3.Bucket('smash-ranking').upload_file(str(Path().home()/'game_dict.json'), game_dict_s3uri)
    table.delete_item(Key={'DataInfo': 'Newest'})
    table.put_item(
        Item={
            "DataInfo": "Newest",
            "date": datestamp,
            "tournament_to_date_dict_s3uri": tournament_to_date_dict_s3uri,
            "game_dict_s3uri": game_dict_s3uri
        }
    )


get_recent_artifacts()
new_tournaments = ['https://www.start.gg/tournament/let-s-make-moves-miami/event/ultimate-singles/matches']
game_dict = update_tournament_cache(new_tournaments)
update_s3_ddb_with_new_artifacts()




python3 -m pip install boto3

python3

get_recent_artifacts()


rankings_dict_elo_games, selected_tournament_urls_elo_games, config_elo_games = get_rankings(start_date=datetime.datetime(2022, 6, 14, 0, 0), end_date=datetime.datetime(2022, 10, 31, 0, 0), top_player_number=None, min_win_loss=1, rankings_to_run=("elo_games"))


rankings_dict_elo_sets, selected_tournament_urls_elo_sets, config_elo_sets = get_rankings(start_date=datetime.datetime(2022, 6, 14, 0, 0), end_date=datetime.datetime(2022, 10, 31, 0, 0), top_player_number=None, min_win_loss=1, rankings_to_run=("elo_sets"))


rankings_dict_h2h_ratio_games, selected_tournament_urls_h2h_ratio_games, config_h2h_ratio_games = get_rankings(start_date=datetime.datetime(2022, 6, 14, 0, 0), end_date=datetime.datetime(2022, 10, 31, 0, 0), top_player_number=None, min_win_loss=1, rankings_to_run=("h2h_ratio_games"))



#insert this stuff into the code
#pull new results!
#run


import json

def utf8len(s):
    return len(s.encode('utf-8'))


utf8len(json.dumps(rankings_dict_h2h_ratio_games,  cls=NpEncoder))







on update call, write to s3 under date folder with checksum
write the path to ddb along with the results s3uri datestamp

make code to find latest games and download






make code to read and write cache stuff to s3
put the list of all tournaments in dynamodb??
make pulling from DDB code


dockerize everything









aws s3 cp ~/game_dict.json s3://smash-ranking/data/game_dict_10292022.json
aws s3 cp ~/tournament_to_date_dict.json s3://smash-ranking/data/tournament_to_date_dict_10292022.json







new_tournaments = ['https://www.start.gg/tournament/ludwig-smash-invitational/event/ultimate-singles-main-event/matches']


game_dict3 = update_tournament_cache(new_tournaments)


new_tournaments = ['https://www.start.gg/tournament/ludwig-smash-invitational/events/ultimate-singles-main-event/brackets/1192747/1844219/matches',
'https://www.start.gg/tournament/ludwig-smash-invitational/events/ultimate-singles-main-event/brackets/1192747/1893382/matches',
'https://www.start.gg/tournament/ludwig-smash-invitational/events/ultimate-singles-main-event/brackets/1233356/1898100/matches']


rankings_dict_ALL, selected_tournament_urls_ALL, config_ALL = get_rankings(start_date=datetime.datetime(2022, 10, 20, 0, 0), end_date=datetime.datetime(2022, 10, 25, 0, 0), top_player_number=None, min_win_loss=1, rankings_to_run=("h2h_ratio_games"))



rankings_dict_ALL, selected_tournament_urls_ALL, config_ALL = get_rankings(start_date=datetime.datetime(2022, 6, 14, 0, 0), end_date=datetime.datetime(2022, 10, 25, 0, 0), top_player_number=None, min_win_loss=1, rankings_to_run=("h2h_ratio_games", "h2h_ratio_sets"))


rankings_dict_ALL, selected_tournament_urls_ALL, config_ALL = get_rankings(start_date=datetime.datetime(2022, 10, 20, 0, 0), end_date=datetime.datetime(2022, 10, 25, 0, 0), top_player_number=None, min_win_loss=1, rankings_to_run=("elo_games", "elo_sets", "h2h_ratio_games", "h2h_ratio_sets"))


rankings_dict_ALL, selected_tournament_urls_ALL, config_ALL = get_rankings(start_date=datetime.datetime(2022, 10, 20, 0, 0), end_date=datetime.datetime(2022, 10, 25, 0, 0), top_player_number=None, min_win_loss=1, rankings_to_run=("elo_games", "elo_sets"))


rankings_dict_ALL, selected_tournament_urls_ALL, config_ALL = get_rankings(start_date=datetime.datetime(2022, 10, 20, 0, 0), end_date=datetime.datetime(2022, 10, 25, 0, 0), top_player_number=None, min_win_loss=1, rankings_to_run=("h2h_ratio_sets"))



player_to_rating_dict_real_sorted = sorted(rankings_dict_elo_games["elo_games"], key=lambda a: a[1], reverse=True)

count = 0
for p, s in player_to_rating_dict_real_sorted:
    if count > 50:
        break
    print(p, s)
    count +=1



player_to_rating_dict_real_sorted = sorted(rankings_dict_elo_sets["elo_sets"], key=lambda a: a[1], reverse=True)

count = 0
for p, s in player_to_rating_dict_real_sorted:
    if count > 50:
        break
    print(p, s)
    count +=1



player_to_rating_dict_real_sorted = sorted(rankings_dict_h2h_ratio_games["h2h_ratio_games"], key=lambda a: a[1], reverse=True)

count = 0
for p, s, v in player_to_rating_dict_real_sorted:
    if count > 50:
        break
    print(p, s, v)
    count +=1



player_to_rating_dict_real_sorted = sorted(rankings_dict_h2h_ratio_sets["h2h_ratio_sets"], key=lambda a: a[1], reverse=True)

count = 0
for p, s, v in player_to_rating_dict_real_sorted:
    if count > 50:
        break
    print(p, s, v)
    count +=1





TODO:
add dynamo logging of the results
make a script to update and increment in s3 and in dynamdb pointer table
make an api that can run both update and compute




MkLeo 28.49011861705026 0.7094011244600398
あcola 28.36245623892716 0.7470275248117836
Sparg0 28.30949625039499 0.6901025266976871
Tea 27.985490668583175 0.7103427766732782
ヨシドラ 27.954033373680044 0.7689572903721574
Tweek 27.891552664610163 0.6943521785256058
Quidd 27.886451369090793 0.7790816165820296
Onin 27.881350902593415 0.724545436442057
Light 27.862901867506615 0.7261488359423013
ProtoBanham 27.84391064828303 0.7358677631305721
Dabuz 27.84055032806997 0.6862003797031607
Shuton 27.83135990841657 0.7423006211602953
Glutonny 27.804173076231024 0.6750213612583413
DDee 27.76364055372527 0.7782174631394675
Sonix 27.743405191960797 0.681686174533864
Riddles 27.665957777392542 0.685368012817593
ミーヤー 27.66276224173817 0.7752618937753243
Etsuji 27.652081659772925 0.8153473512673367
Wrath 27.650594220953636 2.1916222803348275
Kola 27.55500068633885 0.6927205087404669
KEN 27.550276187068455 0.7272833808794955
Maister 27.519346490480732 0.709607844421935
Bloom4Eva 27.514810000749762 0.712742403579078
Asimo 27.436527061197243 0.7378799528175324
quiK 27.414440112878825 0.6983998856678159
へろー 27.411558581059534 0.7239915352376304
zackray 27.39640544308833 0.8471602127727939
MASA 27.39110248988764 0.7515689731624321
Marss 27.35884007974395 0.7088459732923008
Kameme 27.335514904259266 0.7166405759542234
ヤウラ 27.32970434891297 0.7461723611164307
Big D 27.327816351717892 0.7460004382464488
Ouch!? 27.32719252357141 0.746511284627779
ApolloKage 27.322537745464516 0.7565614537545845
Zomba 27.321836410253553 0.699220320874911
Nicko 27.306763720790673 1.5203935033871063
古森霧 27.287407398083847 0.8320376858675584
Kome 27.28330296594388 0.7365760658085386
HIKARU 27.26670080402539 0.7676576585442331
LeoN 27.26493766939109 0.7528380439882798
Sisqui 27.262664302114306 0.6999789403965282





MkLeo 1587.468529542242
あcola 1549.388393602755
Sparg0 1548.875345490184
Tea 1495.916806858748
Tweek 1487.0701349916255
Dabuz 1485.7096986439608
Light 1482.7734528831897
Glutonny 1475.0644085351937
Onin 1473.0773159329
ヨシドラ 1472.5558295362678
Shuton 1471.8678769566839
ProtoBanham 1465.5125516950911
Sonix 1451.4784684050687
Riddles 1449.6985846640791
Kola 1437.685904930852
Maister 1427.1291844469977
ミーヤー 1424.083869274975
KEN 1422.8943068985143
Bloom4Eva 1415.1725372727346
Zomba 1407.5167283614053
Quidd 1405.1551303787935
へろー 1403.2950889680642
Sisqui 1397.2450709509944
ApolloKage 1396.3744938257503
Asimo 1393.9907119176562
zackray 1391.3759812181208
quiK 1391.3180257462088
LeoN 1389.3540631570888
Marss 1388.3222843969677
Anathema 1384.9947308045594
Kameme 1383.9534818057755
Lui$ 1383.8481689944458
MuteAce 1377.652716148084
Ned 1372.8441535787908
Jakal 1372.2198747914938
Gackt 1369.5663882355288
ヤウラ 1366.743220884209
Paseriman 1366.2550355990593





rm ~/game_dict.json
rm ~/tournament_to_date_dict.json
aws s3 cp s3://smash-ranking/data/game_dict_10162022_fix_maesuma_dropnegative.json ~/game_dict.json
aws s3 cp s3://smash-ranking/data/tournament_to_date_dict_10162022_fix_maesuma.json ~/tournament_to_date_dict.json





tournament_to_date_dict = load_json(ALL_TOURNAMENTS_DATES_FILE)
game_dict = load_json(ALL_TOURNAMENTS_GAMES_FILE)
selected_tournament_urls = get_tournaments_from_date_range(tournament_to_date_dict, start_date=datetime.datetime(2022, 6, 1, 0, 0), end_date=datetime.datetime(2022, 10, 19, 0, 0))
all_games = get_game_list_from_list_of_tournaments(game_dict, selected_tournament_urls)
#all_games = convert_game_score_to_winlose_set(all_games)
player_list = get_and_filter_player_list(all_games, top=None, min_win_loss=1)
matchups, player_to_idx = get_matchups(all_games, player_list)

tournament_to_date_dict = load_json(ALL_TOURNAMENTS_DATES_FILE)
game_dict = load_json(ALL_TOURNAMENTS_GAMES_FILE)
selected_tournament_urls = get_tournaments_from_date_range(tournament_to_date_dict, start_date=datetime.datetime(2022, 10, 20, 0, 0), end_date=datetime.datetime(2022, 10, , 0, 0))
all_games = get_game_list_from_list_of_tournaments(game_dict, selected_tournament_urls)





for t, games in game_dict.items():
    for g in games:
        if "Sytonix" in [g[0], g[2]]:
            print(t, g)



for g in all_games:
    if "Sytonix" in [g[0], g[2]]:
            print(t, g)




class LossEq(nn.Module):
    def __init__(self, player_list, matchups, player_to_rating_dict_overall=None):
        super().__init__()
        if player_to_rating_dict_overall is not None:
            rating_list = np.array([float(player_to_rating_dict_overall[player]) if player in player_to_rating_dict_overall else 1000.0  for player in player_list])
            rating_list_normalized = ((rating_list - np.min(rating_list))/np.mean(rating_list))*3+1
            rating_list_normalized_exp = np.power(np.e, rating_list_normalized)
            self.weights = nn.Parameter(torch.Tensor(rating_list_normalized_exp))
        else:
            self.weights = nn.Parameter(torch.Tensor([1.0 for _ in range(len(player_list))]))
        #self.weights = nn.Parameter(torch.Tensor([100.0 for _ in range(num_players)]))
        s1_arr = np.array([float(matchup[2]) for matchup in matchups])
        s2_arr = np.array([float(matchup[3]) for matchup in matchups])
        total_matches_arr = s1_arr + s2_arr
        self.p1_idx_arr = np.array([matchup[0] for matchup in matchups])
        self.p2_idx_arr = np.array([matchup[1] for matchup in matchups])
        self.s1_tensor = torch.tensor(s1_arr)
        self.total_matches_tensor = torch.tensor(total_matches_arr)
        #self.loss = 0
        # for matchup in matchups:
        #     p1_rating = self.weights[matchup[0]]
        #     p2_rating = self.weights[matchup[1]]
        #     p1_estimated_winning_prob = p1_rating/(p1_rating + p2_rating)
        #     self.loss += torch.distributions.binomial.Binomial(float(matchup[2]) + float(matchup[3]), p1_estimated_winning_prob).log_prob(torch.tensor([float(matchup[2])]))
    def forward(self):
        expected_prob_p1_win_tensor = torch.exp(self.weights[self.p1_idx_arr])/(torch.exp(self.weights[self.p1_idx_arr]) + torch.exp(self.weights[self.p2_idx_arr]))
        # for i, num in enumerate(expected_prob_p1_win_tensor.detach().cpu().numpy()):
        #     if not (0 < num < 1):
        #         print(i)
        loss_elem_vect = torch.distributions.binomial.Binomial(self.total_matches_tensor, expected_prob_p1_win_tensor).log_prob(self.s1_tensor)
        loss_val = -torch.sum(loss_elem_vect)
        return loss_val, loss_elem_vect.detach().cpu().numpy()






iters=10000
loss_eq = LossEq(player_list, matchups)
opt = torch.optim.Adam([loss_eq.weights], lr=0.1)
all_losses = []
for i in range(iters):
    opt.zero_grad()
    z, loss_vect = loss_eq()
    z.backward()
    opt.step()
    with torch.no_grad():
        _ = loss_eq.weights.clamp_(1.0, None)
    print(i, float(z))
    all_losses.append(float(z))





ranking_scores_real = loss_eq.weights.detach().cpu().numpy()
player_to_rating_dict_real = {player: rating for player, rating in zip(player_list, ranking_scores_real)}
player_to_rating_dict_real_sorted = sorted(player_to_rating_dict_real.items(), key=lambda a: a[1], reverse=True)

for p, v in player_to_rating_dict_real_sorted:
    print(p, v)







import uuid
# for tourn to date and for gamedict
# make an s3 uri
# upload to s3 date/tourn2date/str(uuid.uuid4()) .json date/gamedict/str(uuid.uuid4()) .json
# put date  and  s3 uri in dynamo db
# write code to pull





for matchup in matchups:
    if matchup[0] == 1225 or matchup[1] == 1225:
        print(matchup)

for i, num in enumerate((torch.exp(loss_eq.weights[loss_eq.p1_idx_arr])/(torch.exp(loss_eq.weights[loss_eq.p1_idx_arr]) + torch.exp(loss_eq.weights[loss_eq.p2_idx_arr]))).detach().cpu().numpy()):
    if not (0 < num < 1):
        print(i)

loss_eq.weights.detach().cpu().numpy()


MkLeo 1531.269651672466
あcola 1513.1031346766388
Sparg0 1479.7076718781836
Light 1443.47183788845
Riddles 1435.504808544603
Dabuz 1434.5605486315171
Tea 1427.8292039064113
Glutonny 1421.4383608050828
Kola 1419.3770617043779
ProtoBanham 1410.4923306797907
Shuton 1398.9469780553634
Maister 1395.7796075977321
Onin 1393.1338650028351
Zomba 1372.7302710461229
Sisqui 1368.0049919502383
Tweek 1366.7664604270901
Sonix 1363.7107175737638
へろー 1357.6767861172768
KEN 1356.9754858037743
ヨシドラ 1351.4457318010209
ミーヤー 1343.2465800077505




MkLeo 28.49011861705026 0.7094011244600398
あcola 28.36245623892716 0.7470275248117836
Sparg0 28.30949625039499 0.6901025266976871
Tea 27.985490668583175 0.7103427766732782
ヨシドラ 27.954033373680044 0.7689572903721574
Tweek 27.891552664610163 0.6943521785256058
Quidd 27.886451369090793 0.7790816165820296
Onin 27.881350902593415 0.724545436442057
Light 27.862901867506615 0.7261488359423013
ProtoBanham 27.84391064828303 0.7358677631305721
Dabuz 27.84055032806997 0.6862003797031607
Shuton 27.83135990841657 0.7423006211602953
Glutonny 27.804173076231024 0.6750213612583413
DDee 27.76364055372527 0.7782174631394675
Sonix 27.743405191960797 0.681686174533864
Riddles 27.665957777392542 0.685368012817593
ミーヤー 27.66276224173817 0.7752618937753243
Etsuji 27.652081659772925 0.8153473512673367
Wrath 27.650594220953636 2.1916222803348275
Kola 27.55500068633885 0.6927205087404669
KEN 27.550276187068455 0.7272833808794955
Maister 27.519346490480732 0.709607844421935
Bloom4Eva 27.514810000749762 0.712742403579078
Asimo 27.436527061197243 0.7378799528175324
quiK 27.414440112878825 0.6983998856678159
へろー 27.411558581059534 0.7239915352376304
zackray 27.39640544308833 0.8471602127727939
MASA 27.39110248988764 0.7515689731624321
Marss 27.35884007974395 0.7088459732923008
Kameme 27.335514904259266 0.7166405759542234
ヤウラ 27.32970434891297 0.7461723611164307
Big D 27.327816351717892 0.7460004382464488
Ouch!? 27.32719252357141 0.746511284627779
ApolloKage 27.322537745464516 0.7565614537545845
Zomba 27.321836410253553 0.699220320874911
Nicko 27.306763720790673 1.5203935033871063
古森霧 27.287407398083847 0.8320376858675584
Kome 27.28330296594388 0.7365760658085386
HIKARU 27.26670080402539 0.7676576585442331
LeoN 27.26493766939109 0.7528380439882798
Sisqui 27.262664302114306 0.6999789403965282





MkLeo 1587.468529542242
あcola 1549.388393602755
Sparg0 1548.875345490184
Tea 1495.916806858748
Tweek 1487.0701349916255
Dabuz 1485.7096986439608
Light 1482.7734528831897
Glutonny 1475.0644085351937
Onin 1473.0773159329
ヨシドラ 1472.5558295362678
Shuton 1471.8678769566839
ProtoBanham 1465.5125516950911
Sonix 1451.4784684050687
Riddles 1449.6985846640791
Kola 1437.685904930852
Maister 1427.1291844469977
ミーヤー 1424.083869274975
KEN 1422.8943068985143
Bloom4Eva 1415.1725372727346
Zomba 1407.5167283614053
Quidd 1405.1551303787935
へろー 1403.2950889680642
Sisqui 1397.2450709509944
ApolloKage 1396.3744938257503
Asimo 1393.9907119176562
zackray 1391.3759812181208
quiK 1391.3180257462088
LeoN 1389.3540631570888
Marss 1388.3222843969677
Anathema 1384.9947308045594
Kameme 1383.9534818057755
Lui$ 1383.8481689944458
MuteAce 1377.652716148084
Ned 1372.8441535787908
Jakal 1372.2198747914938
Gackt 1369.5663882355288
ヤウラ 1366.743220884209
Paseriman 1366.2550355990593







あcola 55.253162
Sparg0 54.348824
MkLeo 54.302258
Onin 53.947796
ミーヤー 53.93845
Tea 53.81441
Light 53.77358
ヨシドラ 53.75401
ProtoBanham 53.690575
DDee 53.66913
Quidd 53.668705
Shuton 53.50403
Riddles 53.441402
Asimo 53.422943
Glutonny 53.418724
Dabuz 53.412975
Kola 53.39443
Bloom4Eva 53.31805
へろー 53.315086
Etsuji 53.308514
Maister 53.233784
ヤウラ 53.221184
Tweek 53.157944
Sonix 53.12943
Big D 53.1215
KEN 53.054565
zackray 53.00811
MASA 52.97036
Nietono 52.81467
Paseriman 52.804
Kameme 52.79478
古森霧 52.771904
たもピオ 52.75525




Sytonix 65.051765
SNACK? 62.267284
Micah 60.66639
あcola 60.055626
Sparg0 59.151142
MkLeo 59.104393
Onin 58.750313
ミーヤー 58.74053
Tea 58.618748
Light 58.573235
ヨシドラ 58.559277
ProtoBanham 58.494812
DDee 58.472622
Quidd 58.466297
Shuton 58.30382
Riddles 58.244705
Asimo 58.228992
Glutonny 58.223976
Dabuz 58.214806
Kola 58.201157
Bloom4Eva 58.119232
へろー 58.1157
Etsuji 58.107265
Maister 58.036083
ヤウラ 58.02204
Tweek 57.96072
Sonix 57.93154
Big D 57.923946
KEN 57.859173
zackray 57.813763
MASA 57.773663
Nietono 57.615517
Paseriman 57.60716
Kameme 57.599728
古森霧 57.573303
たもピオ 57.56051
quiK 57.52909
Jakal 57.527363
AlanDiss 57.44951
Abadango 57.435097
Sisqui 57.435043
Lui$ 57.416737
Zomba 57.388317






あcola 10.752654
MkLeo 10.669915
Sparg0 10.564163
ヨシドラ 10.3853035
ミーヤー 10.370375
Tweek 10.234254
Light 10.223192
Shuton 10.219321
Tea 10.216408
ProtoBanham 10.166087
Dabuz 10.122201
Onin 10.1116905
Glutonny 10.044424
Sonix 9.971065
zackray 9.942571
Bloom4Eva 9.9372015
Riddles 9.935649
Kola 9.896906
へろー 9.864472
ヤウラ 9.850395
Asimo 9.797338
Maister 9.7848835
Kameme 9.774097
KEN 9.76562
HIKARU 9.735973
Kome 9.7075405
Peabnut 9.671587
quiK 9.663477
Jakal 9.658872
Big D 9.633729
れぽ 9.612947
オムアツ 9.600604
Marss 9.592095
Umeki 9.586677
Paseriman 9.585646
Abadango 9.574168






Sparg0 27.80117
MkLeo 27.739048
Shuton 27.51993
ヤウラ 27.338385
ProtoBanham 27.280046
Light 27.201374
Tea 27.17644
Asimo 27.114977
Glutonny 27.103027
Riddles 27.027084
ヨシドラ 27.01147
Maister 26.906664
へろー 26.885054
Sonix 26.83213
Tweek 26.759598
Kola 26.74333
れぽ 26.718853
Dabuz 26.697304
KEN 26.509922
Abadango 26.447763
jaredisking1 26.384188
Kameme 26.360197
Sigma 26.310719
Gackt 26.236944
Paseriman 26.17468
Lea 26.167215
Kome 26.149097
Zomba 26.080078
Sisqui 26.048233
quiK 26.041307
じょうぎぶ 26.001654
Lui$ 25.927237
トウラ 25.83858
SHADIC 25.832176
Cosmos 25.816248






PRE_COVID_tournament_url_to_page_num = {
    'https://smash.gg/tournament/don-t-park-on-the-grass-2018-1/event/smash-ultimate-singles/matches': 78,
    'https://smash.gg/tournament/genesis-6/event/smash-for-switch-singles/matches': 281,
    'https://smash.gg/tournament/frostbite-2019/event/super-smash-bros-ultimate-singles/matches': 166,
    'https://smash.gg/tournament/pound-2019/event/ultimate-singles/matches': 107,
    'https://smash.gg/tournament/momocon-2019-1/event/smash-ultimate-singles/matches': 167,
    'https://smash.gg/tournament/dreamhack-dallas-2019/event/super-smash-bros-ultimate/matches': 66,
    'https://smash.gg/tournament/smash-n-splash-5/event/ultimate-singles/matches': 326,
    'https://smash.gg/tournament/ceo-2019-fighting-game-championships/event/super-smash-bros-ultimate-singles/matches': 156,
    'https://smash.gg/tournament/low-tier-city-7/event/smash-bros-ultimate-1v1/matches': 93,
    'https://smash.gg/tournament/defend-the-north-2019/event/super-smash-bros-ultimate/matches': 59,
    'https://smash.gg/tournament/evo-2019/event/super-smash-bros-ultimate/matches': 472,
    'https://smash.gg/tournament/super-smash-con-2019/event/ultimate-1v1-singles/matches': 361,
    'https://smash.gg/tournament/shine-2019/event/ultimate-singles/matches': 118,
    'https://smash.gg/tournament/the-big-house-9/event/ultimate-singles/matches': 136,
    'https://smash.gg/tournament/dreamhack-atlanta-2019/event/smash-ultimate-1v1/matches': 86,
    'https://smash.gg/tournament/2gg-kongo-saga/event/ultimate-singles/matches': 225,
    'https://smash.gg/tournament/let-s-make-big-moves-a-tristate-smash-ultimate-national/event/smash-ultimate-1v1/matches': 87,
    'https://smash.gg/tournament/genesis-7-1/event/ultimate-singles/matches': 227,
    'https://smash.gg/tournament/frostbite-2020/event/super-smash-bros-ultimate-1v1-singles/matches': 171,
    'https://smash.gg/tournament/ceo-dreamland-2020/event/smash-ultimate-1v1/matches': 68,
    'https://smash.gg/tournament/smash-ultimate-summit/event/ultimate-singles/matches': 4,
    'https://smash.gg/tournament/smash-ultimate-summit-2/event/smash-ultimate-summit/matches': 4
}


#https://chromedriver.storage.googleapis.com/index.html?path=103.0.5060.53/

POST_COVID_tournament_url_to_page_num = {
    'https://smash.gg/tournament/smash-ultimate-summit-3/event/ultimate-singles/matches': 4,
    'https://smash.gg/tournament/riptide-3/event/ultimate-singles/matches': 137,
    'https://smash.gg/tournament/glitch-8-5-konami-code/event/ultimate-singles/matches': 56,
    'https://smash.gg/tournament/low-tide-city-2021/event/smash-bros-ultimate-1v1/matches': 147,
    'https://smash.gg/tournament/super-smash-con-fall-fest/event/ultimate-1v1-singles/matches': 103,
    'https://smash.gg/tournament/port-priority-6/event/ultimate-singles/matches': 86,
    'https://smash.gg/tournament/mainstage-2021/event/ultimate-singles/matches': 111,
    'https://smash.gg/tournament/the-smash-world-tour-championships/event/ultimate-lcq-friday/matches': 61,
    'https://smash.gg/tournament/the-smash-world-tour-championships/event/ultimate-championships/matches': 8,
}




SWT_data = {
    'https://smash.gg/tournament/the-smash-world-tour-championships/event/ultimate-championships/matches': 8,
    'https://smash.gg/tournament/the-smash-world-tour-championships/event/ultimate-lcq-friday/matches': 61
}



jp_tournaments = {
    'https://smash.gg/tournament/swt-east-asia-ultimate-regional-finals/event/ultimate-singles/matches': 4,
    'https://smash.gg/tournament/top-6-maesumatop-6-1on1/event/singles-tournament/matches': 43,
    'https://smash.gg/tournament/6-kagaribi-6/event/singles/matches': 103,
    'https://smash.gg/tournament/5-kagaribi-5-1/event/singles-1/matches': 69,
    'https://smash.gg/tournament/8-11/event/singles/matches': 34,
    'https://smash.gg/tournament/3-kagaribi-3/event/singles/matches': 24,
    'https://smash.gg/tournament/4-kagaribi-4-1/event/singles/matches': 52
}




# vca vienna challengers 2021
# lets make big moves 2022
# glitch infinite
# smash ultimate summit 4
# g4 smash invitational?
# collision 2022
# delfino maza reta 2022
# genesis 8
# pound 2022
# e caribana
# colossal 2022
# momocon 2022
# battle of bc
# crown 2
# get on my level 2022
# gimvitational
# ceo 2022
# low tide city 2022
# double down 2022
#


# maesuma 7
# kagaribi 7
# maesuma 8






