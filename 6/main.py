import copy
# Open file
puzzle = open("input.txt", "r")
puzzle_data = puzzle.read()
# Cycle through strings of 4 to find start of packet
for x in range(0, len(puzzle_data)-3):
    buffer = puzzle_data[x:x+4]
    if len(buffer) == len(set(buffer)):
        sop = x+4
        break
# Cycle through strings of 14 (after start of packet) to find start of message
for y in range(sop-4, len(puzzle_data)-13):
    message = puzzle_data[y:y+14]
    if len(message) == len(set(message)):
        som = y+14
        break
# Print solution
print("The solution to part 1 is ", sop)
print("The solution to part 2 is ", som)