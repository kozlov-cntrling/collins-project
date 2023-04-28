from stats import List

def calculate_OPS(player_stats: List):
    OPS_list = []

    for list in player_stats:
        #OBP portion
        on_base_percentage = (list[7] + list[12] + list[16]) / (list[5] + list[12] + list[16] + list[17]) 
        #slugging portion
        #catches if at bat = 0
        if list[5] != 0:
            slugging_decimal = (list[7] + (list[8] * 2) + (list[9]*3) + (list[10] * 4) / list[5])
            OPS_list.append((list[0], list[1], round((on_base_percentage + slugging_decimal),1)))
        else:
            OPS_list.append(list[0], list[1], round(on_base_percentage,1))
    return OPS_list
        
        