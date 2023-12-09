# # The test input (parsed_directly)
# test_time = 71530
# test_distance = 940200

# # The actual input
# time = [44707080]
# distance = [283113411341491]
 
# # Total number of ways for each race
# #NUM_OF_WAYS = []

# # Loop over the given set of races
# #for limit, record in zip(test_time, test_distance):
#     # Ways to win the race
# ways = 0
# # Get all the options
# for hold_time in range(0, test_time + 1):
#     # Race setup
#     # Initial speed of the boat (in ms)
#     boat_speed = 0
#     # Race time clock in ms
#     clock = 0
#     # Distance travelled by boat (in mm)
#     dist_covered = 0
#     # For every second held, increase boat speed and clock time
#     while hold_time > 0:
#         boat_speed += 1
#         hold_time -= 1
#         clock += 1

#     # Actual race
#     # Until limit of the race is hit, increment clock
#     while clock < test_time:
#         # Increase distance based on speed per ms
#         dist_covered += boat_speed
#         clock += 1
#     #print(boat_speed, dist_covered)
#     if dist_covered > test_distance:
#         ways += 1

# # product = 1
# # #print(NUM_OF_WAYS)
# # for num in NUM_OF_WAYS:
# #     product *= num
# #print(f"Product of number of ways is {product}")

# print(f"The number of ways is ",ways)


roots = []
test_limit = 71530
test_record = 940200

limit = 44707080
record = 283113411341491

for hold_time in range (0, limit + 1):
    boat_speed = hold_time
    time_left = limit - hold_time 
    dist_covered = boat_speed * time_left
    if dist_covered > record:
        roots.append(hold_time)
        roots.append(limit - hold_time)
        break

# for hold_time in range (limit + 1, 0, -1):
#     boat_speed = hold_time
#     clock = hold_time
#     dist_covered = 0
#     while clock < limit:
#         dist_covered += boat_speed
#         clock += 1
#     if dist_covered > record:
#         roots.append(hold_time)
#         break

print(roots)
print(roots[1] - roots[0] + 1)