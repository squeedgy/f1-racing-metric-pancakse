import pandas as pd
import json

with open('data/race_results/2023_race1.json') as f:
    data = json.load(f)

df = pd.json_normalize(data)

numeric_columns = ["number", "position", "points", "grid", "laps", "Driver.permanentNumber", "FastestLap.rank", "FastestLap.lap"]
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

df['FastestLap.AverageSpeed.speed'] = pd.to_numeric(df['FastestLap.AverageSpeed.speed'], errors='coerce')

df['position'] = pd.to_numeric(df['position'], errors='coerce').astype('Int64')

kph_to_mph_conversion_factor = 0.621371
df['FastestLap.AverageSpeed.mph'] = df['FastestLap.AverageSpeed.speed'] * kph_to_mph_conversion_factor
df['FastestLap.AverageSpeed.mph'] = round(df['FastestLap.AverageSpeed.mph'], 2)

df.to_json('data/race_results/2023_race1_formatted.json', orient='records', default_handler=str, indent=2)
