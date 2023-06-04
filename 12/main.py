# Read input
puzzle_input = open("input.txt", "r")
input_data = puzzle_input.read()
input_list = input_data.split("\n")
input_list.pop(-1)
for line in range(0, len(input_list)):
    # Extract start and replace with the lowest altitude
    for column in range(0,len(input_list[line])):
        if input_list[line][column] == 'S':
            start = (line, column, 1)
            input_list[line] = input_list[line].replace('S', 'a')
    # Extract end and replace with the highest altitude
    for column in range(0,len(input_list[line])):
        if input_list[line][column] == 'E':
            finish = (line, column, 26)
            input_list[line] = input_list[line].replace('E', 'z')
# Define breadth-first search function
def bfs(start_tile, end_condition, direction):
    # Initialise local variables
    found = False
    distance = 0
    candidates = [start_tile]
    queue = set()
    traversed = set()
    # Determine movement direction
    match direction:
        case 'ascending':
            step = '<= tile[2] + 1'
        case 'descending':
            step = '>= tile[2] - 1'
    # Test if end condition has not been fulfilled yet
    while not found:
        # If candidates list has tiles, visit tiles
        if candidates:
            for tile in candidates:
                # Move current tile from candidates to traversed
                candidates.remove(tile)
                traversed.add(tile)
                # If the tile meets the end condition, signal this and return distance
                if eval(end_condition):
                    found = True
                    return distance
                # Otherwise add neighbours to queue if they are visitable and not already in queue or traversed
                else:
                    if tile[1] < len(input_list[0]) - 1:
                        east = (tile[0], tile[1] + 1, ord(input_list[tile[0]][tile[1] + 1]) - 96)
                        if east not in traversed and eval('east[2] ' + step):
                            queue.add(east)
                    if tile[0] < len(input_list) - 1:
                        south = (tile[0] + 1, tile[1], ord(input_list[tile[0] + 1][tile[1]]) - 96)
                        if south not in traversed and eval('south[2] ' + step):
                            queue.add(south)
                    if tile[1] > 0:
                        west = (tile[0], tile[1] - 1, ord(input_list[tile[0]][tile[1] - 1]) - 96)
                        if west not in traversed and eval('west[2] ' + step):
                            queue.add(west)
                    if tile[0] > 0:
                        north = (tile[0] - 1, tile[1], ord(input_list[tile[0] - 1][tile[1]]) - 96)
                        if north not in traversed and eval('north[2] ' + step):
                            queue.add(north)
        # If candidates list empty, move tiles from queue to candidates
        else:
            candidates = list(queue)
            queue = set()
            distance += 1
# Solve part 1
distance_part1 = bfs(start, 'tile == finish', 'ascending')
# Solve part 2
distance_part2 = bfs(finish, 'tile[2] == 1', 'descending')
# Print solutions
print("The solution to part 1 is", distance_part1)
print("The solution to part 2 is", distance_part2)