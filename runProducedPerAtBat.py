from stats import List

def calculate_runs_produced_per_at_bat(player_stats: List):
    # list of returns
    runs_produced_per_at_bat = []
    
    for list in player_stats:
        # calculate total bases
        total_bases = list[6] + (list[8] * 2) + (list[9] * 3) + (list[10] * 4)
        
        # calculate runs produced per at-bat
        if list[5] != 0:
            runs_produced_per_at_bat_value = round(((list[6] + list[11]) / list[5]), 4)
            runs_produced_per_at_bat.append((list[0], list[1], runs_produced_per_at_bat_value))
        else:
            runs_produced_per_at_bat.append((list[0], list[1], "has no at-bats."))

    return runs_produced_per_at_bat