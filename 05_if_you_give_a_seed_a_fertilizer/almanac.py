from pprint import pprint

def main():
    with open("test_input.txt") as file:
        for line in file:
            #pprint(line)
            parse_input(line, file)


def parse_input(line, file):
    if line.startswith("seeds:"):
        seeds = line.split(":")[1]
        seeds = seeds.split(" ")
        print(seeds)
    elif line.startswith("seed-to-soil"):
        seed_soil = get_values(file)
        print(seed_soil)
    elif line.startswith("soil-to-fertilizer"):
        soil_fert=  get_values(file)
        print(soil_fert)
    elif line.startswith("fertilizer-to-water"):
        fert_water = get_values(file)
        print(fert_water)
    elif line.startswith("water-to-light"):
        water_light = get_values(file)
        print(water_light)
    elif line.startswith("light-to-temperature"):
        light_temp = get_values(file)
        print(light_temp)
    elif line.startswith("temperature-to-humidity"):
        temp_humid = get_values(file)
        print(temp_humid)
    elif line.startswith("humidity-to-location"):
        humid_loc = get_values(file)
        print(humid_loc)

def get_values(file):
    values = []
    next_line = next(file)
    while next_line != "\n":
        values.append(next_line)
        next_line = next(file)
    return values

if __name__ == "__main__":
    main()
