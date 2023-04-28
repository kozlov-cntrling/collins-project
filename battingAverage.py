from stats import List

def calculate_batting_average(player_stats: List):
    #list of returns
    batting_averages = []
    
    for list in player_stats:
        #error catch if attempting to divide by 0 at index 9
        if list[9] != 0:
            batting_average = round(((list[7] / list[5]) * 100),4)
            batting_percent = str(batting_average) + "%"
            batting_averages.append((list[0], list[1], batting_percent))
        else:
            batting_averages.append((list[0], list[1],"has no at-bats."))


    return batting_averages
