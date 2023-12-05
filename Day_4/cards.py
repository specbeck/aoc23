import re 

def main():
    with open("test_input.txt") as file:
        for line in file:
            parse_line(line)

def parse_line(line):
    sections = line.split(":")
    numbers = sections[1]
    numbers = numbers.split("|")
    
    winning_nums = numbers[0]
    winning_nums = winning_nums.split(" ") 
    

    print(sections)


if __name__ == "__main__":
    main()