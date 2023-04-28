from stats import List

def calculate_slugging_percentage(player_stats: List):
    #future return value
    slugging_percents = []

    for list in player_stats:
        #catches if at bat = 0
        if list[5] != 0:
            slugging_decimal = round((list[7] + (list[8] * 2) + (list[9]*3) + (list[10] * 4) / list[5]),3)
            slugging_string = str(slugging_decimal) + "%"
            
            slugging_percents.append((list[0], list[1], slugging_string))
        else:
            slugging_percents.append((list[0], list[1],"has no slugging percentage"))

    return slugging_percents
