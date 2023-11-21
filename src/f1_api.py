import requests

BASE_URL = "https://ergast.com/api/f1"

def get_seasons():
    seasons = ["2023"]
    return seasons

def get_race_results(season, round):
    url = f"{BASE_URL}/{season}/{round}/results.json"
    response = requests.get(url)
    data = response.json()
    return data["MRData"]["RaceTable"]["Races"][0]["Results"]