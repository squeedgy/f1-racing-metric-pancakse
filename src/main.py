import json
from f1_api import get_race_results

def export_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=2)

selected_season = "2023"
selected_round = "1"

race_results = get_race_results(selected_season, selected_round)
print(f"Race Results for {selected_season}, Round {selected_round}:", race_results)

export_to_json(race_results, f'data/race_results/{selected_season}_race{selected_round}.json')
