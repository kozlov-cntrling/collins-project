from stats import List

def calculate_on_base_percentage(player_stats: List):
    # stores list of returns
    on_base_percentages = []

    for list in player_stats:
        #calculations
        on_base_decimal = (list[7] + list[12] + list[16]) / (list[5] + list[12] + list[16] + list[17])
        on_base_percent = round(on_base_decimal * 100, 1)
        #appends as a percentage instead of decimal
        on_base_string = str(on_base_percent) + "%"

        on_base_percentages.append((list[0], list[1], on_base_string))
    
    return on_base_percentages