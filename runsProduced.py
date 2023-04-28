from stats import List

def calculate_runs_produced(player_stats: List):
    runs_produced = []
    
    for list in player_stats:
        # calculate total bases
        total_bases = list[7] + (list[8] * 2) + (list[9] * 3) + (list[10] * 4)
 
        # calculate runs produced
        runs_produced_value = round(((list[7] + list[12]) * total_bases) / (list[5] + list[12]),4)
        runs_produced.append((list[0], list[1], runs_produced_value))
    
    return runs_produced