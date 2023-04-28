from stats import List as playerStats

from battingAverage import calculate_batting_average
from onBasePercent import calculate_on_base_percentage
from OPS import calculate_OPS
from runsProduced import calculate_runs_produced
from runProducedPerAtBat import calculate_runs_produced_per_at_bat
from sluggingPercent import calculate_slugging_percentage


print("1. Batting average\n2. Slugging percentage\n3. On Base percentage\n4. OPS (On Base + Slugging)\n5. Runs Produced\n6. Runs Produced per At Bat")
while True:
    user_input = int(input("Choose which statistic you'd like to see:"))

    if user_input == 1:
        print(calculate_batting_average(playerStats))

    if user_input == 2:
        print(calculate_slugging_percentage(playerStats))

    if user_input == 3:
        print(calculate_on_base_percentage(playerStats))

    if user_input == 4:
        print(calculate_OPS(playerStats))

    if user_input == 5:
        print(calculate_runs_produced(playerStats))

    if user_input == 6:
        print(calculate_runs_produced_per_at_bat(playerStats))