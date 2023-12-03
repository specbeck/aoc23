from pprint import pprint
import string


SCHEMATIC = []
TOTAL = 0
CHARACTERS = list(string.punctuation)


def main():
    with open("test_input.txt") as file:
        for line in file:
            render_map(line)
    check_vicinity()
    #pprint(SCHEMATIC)
    print(TOTAL)

def render_map(line):
    row = []
    num = ""
    for char in line:
        if char.isdigit():
            num += char
        else:
            if num != "":
                row.append(num)
                num = ""
            row.append(char)
    SCHEMATIC.append(row)


def check_vicinity():
    global TOTAL
    for rowno, row in enumerate(SCHEMATIC):
        charno = 0
        for colno, val in enumerate(row):
            charno += len(val)
            print(charno)
            if val.isnumeric():
                #print(val)
                lower_row_neighbours = []
                upper_row_neighbours = []
                row_neighbours = [row[colno -1], row[colno +1]]
                
                if (rowno - 1) > 0:
                    upper_row = SCHEMATIC[rowno - 1]
                    for i in range(charno - len(val) - 1 , charno + 1):
                        if i < len(upper_row):
                            upper_row_neighbours.append(upper_row[i])
                
                if (rowno + 1) < len(SCHEMATIC):
                    lower_row = SCHEMATIC[rowno + 1]
                    for j in range(charno - len(val) - 1 , charno + 1):
                        if j < len(lower_row):
                            lower_row_neighbours.append(lower_row[j])
                
                neighbours = [lower_row_neighbours, row_neighbours, upper_row_neighbours]
                #print(neighbours)
                for neighbour in neighbours:
                    if neighbour in CHARACTERS:
                        if neighbour != "." and neighbour != "\n":
                            TOTAL += int(val)
                            break


                # print(val)
                # for i in range(rowno - 1, rowno + 2):
                #     for j in range(colno - 1, colno + len(val)):
                #         if i >= 0 and j >= 0:
                #             print(i, j)
                #             if (SCHEMATIC[i][j]) in ['*', '#', '+', "$"]:
                #                 # print(val)
                #                 TOTAL += int(val)




if __name__ == "__main__":
    main()