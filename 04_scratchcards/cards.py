COPIES = {}
MATCHES = {}
TOTAL_SCRATCHCARDS = 0

def main():
    global TOTAL_SCRATCHCARDS
    with open("test_input.txt") as file:
        for line in file:
            cardno, win, draw = parse_line(line)
            COPIES[cardno] = 0
            get_matches(cardno, win, draw)
            #scratchcards.append(calculate_points(win, draw))

    #print(f"The scratchcards are worth {sum(scratchcards)} points!")
    get_initial_copies()
    for copy in COPIES:
        if COPIES[copy] > 0:
            while COPIES[copy] > 0:
                get_copy_of_copies(copy)
                COPIES[copy] -= 1
                
    print("The total number of scratchcards we end up with are", TOTAL_SCRATCHCARDS)


def parse_line(line):
    global TOTAL_SCRATCHCARDS
    TOTAL_SCRATCHCARDS += 1 
    sections = line.split(":")
    card = sections[0].split(" ")
    card_number = card[-1]
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

    return card_number, parsed_win, parsed_lot


def get_matches(card_num, winning, drawing):
    matches = 0
    for num in drawing:
        if num in winning:
            matches += 1
    MATCHES[card_num] = matches
    

def get_initial_copies():
    global TOTAL_SCRATCHCARDS
    for card in MATCHES:
        if MATCHES[card] > 0:
            for i in range(1, MATCHES[card] + 1):
                i = i + int(card)
                #print(i)
                COPIES[f'{i}'] += 1
        TOTAL_SCRATCHCARDS += COPIES[card]

def get_copy_of_copies(card):
    global TOTAL_SCRATCHCARDS
    for i in range(1, MATCHES[card] + 1):
        i = i + int(card)
        #print(i)
        COPIES[f'{i}'] += 1
        TOTAL_SCRATCHCARDS += 1


def calculate_points(winning, drawing):
    matches = -1
    for num in drawing:
        if num in winning:
            #print(num)     
            matches += 1

    if matches == 0:
        points = 1
    elif matches == -1:
        points = 0
    else:
        points = 2 ** matches
    return points


if __name__ == "__main__":
    main()