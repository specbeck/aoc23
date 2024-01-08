from pprint import pprint
import string

SCHEMATIC = []
SKELETON = []
PARTSUM = 0
GEARSUM = 0
CHARACTERS = list(string.punctuation)


def main():
    with open("test_input.txt") as file:
        for line in file:
            render_map(line)
            render_dummy_map(line)
    check_vicinity()
    #pprint(SCHEMATIC)
    #print(SKELETON)
    print(f"The sum of all part numbers in the schematic is: {PARTSUM}")
    print(f"The sum of all gear ratios in the schematic is: {GEARSUM}")

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


def render_dummy_map(line):
    return SKELETON.append([char for char in line])


def check_vicinity():
    global PARTSUM
    for rowno, row in enumerate(SCHEMATIC):
        charno = 0
        for colno, val in enumerate(row):
            charno += len(val)
            if val.isnumeric():
                lower_row_neighbours = []
                upper_row_neighbours = []
                row_neighbours = [row[colno -1], row[colno +1]]
                
                if (rowno - 1) >= 0:
                    upper_row = SKELETON[rowno - 1]
                    for i in range(charno - len(val) - 1 , charno + 1):
                        if i < len(upper_row):
                            upper_row_neighbours.append(upper_row[i])
                
                if (rowno + 1) < len(SKELETON):
                    lower_row = SKELETON[rowno + 1]
                    for j in range(charno - len(val) - 1 , charno + 1):
                        if j < len(lower_row):
                            lower_row_neighbours.append(lower_row[j])
                
                neighbours = [*lower_row_neighbours, *row_neighbours, *upper_row_neighbours]
                for neighbour in neighbours:
                    if neighbour in CHARACTERS:
                        if neighbour != "." and neighbour != "\n":
                            PARTSUM += int(val)
                            break
            
            # The faulty gear?
            if val == "*":
                lower_row_neighbours = []
                upper_row_neighbours = []
                row_neighbours = [row[colno -1], row[colno +1]]

                if (rowno - 1) >= 0:
                    upper_row = SKELETON[rowno - 1]
                    actual_row = SCHEMATIC[rowno - 1]
                    num = ""
                    for i in range(charno - len(val) - 1 , charno + 1):
                        if i < len(upper_row):
                            print(find_actual_index(actual_row, i))
                            if upper_row[i].isdigit():
                                j = i
                                while upper_row[j].isdigit():
                                    num += upper_row[j]
                                    j = j - 1
                                num = num[::-1]
                                while upper_row[j].isdigit():
                                    num += upper_row[j]
                                    j = j + 1
                            else:
                                if num != "":
                                    upper_row_neighbours.append(num)
                                    num = ""
                                upper_row_neighbours.append(upper_row[i])
                
                if (rowno + 1) < len(SKELETON):
                    lower_row = SKELETON[rowno + 1]
                    num = ""
                    for j in range(charno - len(val) - 1 , charno + 1):
                        if j < len(lower_row):  
                            if lower_row[i].isdigit():
                                j = i
                                while lower_row[j].isdigit():
                                    num += lower_row[j]
                                    j = j - 1
                                num = num[::-1]
                                while lower_row[j].isdigit():
                                    num += lower_row[j]
                                    j = j + 1
                            else:
                                if num != "":
                                    lower_row_neighbours.append(num)
                                    num = ""
                                lower_row_neighbours.append(lower_row[i])
                        
                neighbours = [lower_row_neighbours, row_neighbours, upper_row_neighbours]
                print(neighbours)

def find_actual_index(row, charno):
    index = 0
    char_count = 0
    print(row)
    for char in row:
        #print(char)
        while char_count <= charno:
            if char.isnumeric():
                index += len(char) - (len(char) - 1)
                char_count += len(char)
            else:
                index += 1
                char_count += 1
    return index


if __name__ == "__main__":
    main()