import json
import random

with open('data/race_results/2023_race1_formatted.json', 'r') as file:
    data = json.load(file)

race_points = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
sprint_points = [8, 7, 6, 5, 4, 3, 2, 1]

num_simulations = 1000

simulated_total_points = {}

for _ in range(num_simulations):
    for entry in data:
        driver_id = entry["Driver.driverId"]
        position = random.randint(1, len(race_points))
        fastest_lap_rank = random.randint(1, 10)

        if position <= len(race_points):
            points = min(race_points[position - 1], max(race_points))
            simulated_total_points[driver_id] = simulated_total_points.get(driver_id, 0) + points

        if fastest_lap_rank <= 10:
            simulated_total_points[driver_id] = simulated_total_points.get(driver_id, 0) + min(1, 1)

simulated_ranked_drivers = sorted(simulated_total_points.items(), key=lambda x: x[1], reverse=True)

for position, (driver_id, points) in enumerate(simulated_ranked_drivers, start=1):
    print(f"Simulated Position {position}: {driver_id} - Simulated Total Points: {points}")