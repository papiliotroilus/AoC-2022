# Read input line by line
with open('input.txt') as puzzle:
    for puzzle_line in puzzle:
        puzzle_line = puzzle_line.rstrip('\r\n')
    if puzzle_line == "whatever":
        pass
    elif puzzle_line == "whatever else":
        pass
# Read input entirely
puzzle = open("input.txt", "r")
puzzle_data = puzzle.read()
input_list = puzzle_data.split("\n")
input_list.pop(-1)
# Print solutions
print("The solution to part 1 is", 1)
print("The solution to part 2 is", 2)