import json

with open('data/race_results/2023_race1_formatted.json', 'r') as file:
    data = json.load(file)

race_points = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1, 1]
sprint_points = [8, 7, 6, 5, 4, 3, 2, 1]

total_points = {}
average_speeds = {}
race_times = {}

for entry in data:
    driver_id = entry["Driver.driverId"]
    position = entry["position"]
    fastest_lap_rank = entry["FastestLap.rank"]
    fastest_lap_time_str = entry["FastestLap.Time.time"]
    average_speed_str = entry["FastestLap.AverageSpeed.speed"]

    fastest_lap_time_ms = int(float(fastest_lap_time_str.replace(':', '').replace('.', '')) * 1000)
    average_speed = float(average_speed_str)

    if position <= len(race_points):
        total_points[driver_id] = total_points.get(driver_id, 0) + race_points[position - 1]

    if fastest_lap_rank <= 10:
        total_points[driver_id] = total_points.get(driver_id, 0) + 1

    if "Sprint" in entry and entry["Sprint"]["position"] <= len(sprint_points):
        total_points[driver_id] = total_points.get(driver_id, 0) + sprint_points[entry["Sprint"]["position"] - 1]

    distance = average_speed * fastest_lap_time_ms

    average_speeds[driver_id] = average_speed
    race_times[driver_id] = distance / average_speed

ranked_drivers = sorted(total_points.items(), key=lambda x: x[1], reverse=True)

for position, (driver_id, points) in enumerate(ranked_drivers, start=1):
    print(f"Position {position}: {driver_id} - Total Points: {points} - Race Time: {race_times[driver_id]} seconds - Average Speed: {average_speeds[driver_id]} kph")