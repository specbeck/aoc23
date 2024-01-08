import re

def main():
    hands = get_hands("test_input.txt")
    print(hands)
    get_hand_type(["2AAAA", 45])

def get_hands(filename: str):
    """Parses the input from the given filename and returns a list of hands"""
    hands = []
    with open(filename) as file:
        for line in file:
            hand = line.split(" ")
            hand[1] = int(hand[1])
            hands.append(hand)
    return hands

def get_hand_type(hand):
    set_of_values = "2-9AKQJT"
    value = hand[0]
    if re.search(f'[{set_of_values}]{5}', value):
        print("Five of a kind!")
    elif re.search(f'[.*{set_of_values}]{4}.*', value):
        print("here")

if __name__ == "__main__":
    main()