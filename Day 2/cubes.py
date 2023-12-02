from pprint import pprint
GAMES = {}
BAG_LIMIT = (12, 13, 14)

def main():
    with open('input.txt') as file:
        for line in file:
            parse_game(line)
    print(f"The sum of IDs of possible games is: {check_possible(GAMES)}" )


def parse_game(line):
    line_as_list = line.split(" ")
    
    all_sets = []

    # Tuple for red, green and blue cubes (in order)
    rgb_tuple = [0, 0, 0]
    for index, value in enumerate(line_as_list):
        
        if "red" in value:
            rgb_tuple[0] += int(line_as_list[index - 1])

        if "green" in value:
            rgb_tuple[1] += int(line_as_list[index - 1])
        if "blue" in value:
            rgb_tuple[2] += int(line_as_list[index - 1])
        if ";" in value:
            all_sets.append(rgb_tuple)
            rgb_tuple = [0, 0, 0]
        else:
            pass
    all_sets.append(rgb_tuple)


    GAMES[int(line_as_list[1].removesuffix(":"))] = all_sets


def check_possible(games):
    possible_games = 0
    for game_number in games:
        possible = True
        sets = games[game_number]
        for set in sets:
            for value, limit in zip(set, BAG_LIMIT):
                if value > limit:
                    possible = False
        if possible == True:
            possible_games += game_number
            
    return possible_games

if __name__ == "__main__":
    main()