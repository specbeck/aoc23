import re 
SUM = 0

def main():
    with open("test_input.txt") as file:
        scratchcards = []
        for line in file:
            win, draw = parse_line(line)
            scratchcards.append(calculate_points(win, draw))
    
    print(f"The scratchcards are worth {sum(scratchcards)} points!")



def parse_line(line):
    sections = line.split(":")
    numbers = sections[1]
    numbers = numbers.split("|")
    
    winning_nums = numbers[0]
    lottery_nums = numbers[1]
    winning_nums = winning_nums.split(" ") 
    lottery_nums = lottery_nums.split(" ")

    winning_nums = [num.strip(" \n") for num in winning_nums]
    lottery_nums = [num.strip(" \n") for num in lottery_nums]

    parsed_win = []
    parsed_lot = []

    for num in winning_nums:
        if num == "":
            pass
        else:
            parsed_win.append(int(num))
    for num in lottery_nums:
        if num == "":
            pass
        else:
            parsed_lot.append(int(num))
    #winning_nums = [int(num) for num in winning_nums]
    #lottery_nums = [int(num) for num in lottery_nums]


    return parsed_win, parsed_lot

def calculate_points(winning, drawing):
    points = 0
    value = 1
    consecutive_matches = 0
    for i, num in enumerate(drawing):
        if num in winning:
            #print(num)
            consecutive_matches += 1
            for _ in range(1, consecutive_matches + 1):
                value *= 2
            points += value
        consecutive_matches = 0
    #print(points)
    return points


if __name__ == "__main__":
    main()