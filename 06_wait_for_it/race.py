# The test input (parsed_directly)
test_time = [7, 15, 30]
test_distance = [9, 40, 200]

# The actual input
time = [44, 70, 70, 80]
distance = [283  , 1134  , 1134  , 1491]
 
# Total number of ways for each race
NUM_OF_WAYS = []

# Loop over the given set of races
for limit, record in zip(time, distance):
    # Ways to win the race
    ways = 0
    # Get all the options
    for hold_time in range(0, limit + 1):
        # Race setup
        # Initial speed of the boat (in ms)
        boat_speed = 0
        # Race time clock in ms
        clock = 0
        # Distance travelled by boat (in mm)
        dist_covered = 0
        # For every second held, increase boat speed and clock time
        while hold_time > 0:
            boat_speed += 1
            hold_time -= 1
            clock += 1

        # Actual race
        # Until limit of the race is hit, increment clock
        while clock < limit:
            # Increase distance based on speed per ms
            dist_covered += boat_speed
            clock += 1
        #print(boat_speed, dist_covered)
        if dist_covered > record:
            ways += 1
    
    NUM_OF_WAYS.append(ways)

product = 1
#print(NUM_OF_WAYS)
for num in NUM_OF_WAYS:
    product *= num
print(f"Product of number of ways is {product}")