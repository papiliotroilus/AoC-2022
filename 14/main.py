# Function for simulating sand
def simulate_sand(sand_map):
    # Initialise variables
    keep_falling = True
    floor_not_reached = True
    source_open = True
    cycle = 0
    floor_cycle = 0
    map_offset = 0
    # Iterate through falling sand units until source is blocked
    while source_open:
        # Initialise sand unit at source coordinate
        sand_vert = 0
        sand_hor = 500 - min(cave_hor) + map_offset
        # Iterate through positions on map until sand unit is at rest
        while keep_falling:
            # If floor of cave is reached, sand unit is at rest
            if sand_vert == len(sand_map) - 1:
                keep_falling = False
            # If there is an empty space underneath, sand unit falls
            elif sand_map[sand_vert + 1][sand_hor] == ".":
                sand_vert += 1
            # If sand unit reaches left edge, extend the map and increase horizontal coordinate offset
            elif sand_hor == 0:
                for map_row in sand_map:
                    map_row.insert(0, '.')
                map_offset += 1
            # If there is an empty space down and to the left, sand unit falls leftwards
            elif sand_map[sand_vert + 1][sand_hor - 1] == ".":
                sand_vert += 1
                sand_hor -= 1
            # If sand unit reaches right edge, extend the map
            elif sand_hor == len(sand_map[0]) - 1:
                for map_row in sand_map:
                    map_row.append('.')
            # If there is an empty space down and to the right, sand unit falls rightwards
            elif sand_map[sand_vert + 1][sand_hor + 1] == ".":
                sand_vert += 1
                sand_hor += 1
            # Finally, if there are no moves available, sand unit is at rest
            else:
                keep_falling = False
        # Add sand point to map
        sand_map[sand_vert][sand_hor] = "o"
        # Detect when the floor is reached for part 1 solution
        if floor_not_reached and sand_vert == len(sand_map) - 1:
            floor_cycle = cycle
            floor_not_reached = False
        # Detect when source is blocked for part 2 solution
        if (sand_vert == 0) and (sand_hor == 500 - min(cave_hor) + map_offset):
            source_open = False
        cycle += 1
        # Map visualisation for debugging
        # for map_row in sand_map:
        #     print(*map_row)
        # print("finished cycle",cycle)
        keep_falling = True
    # Return solutions for part 1 and 2
    return floor_cycle, cycle


# Initialise list of rock coordinates
rock_points = set()
# Read input line by line
with open('input.txt') as puzzle:
    for puzzle_line in puzzle:
        # Convert each line to a list of rock line vertices
        rock_strings = puzzle_line.rstrip('\r\n').split(" -> ")
        rock_tuples = [tuple(map(int, string.split(','))) for string in rock_strings]
        # Expand vertices to point coordinates of full line and add them to list of rock points
        for i in range(0, len(rock_tuples) - 1):
            rock_segment = (rock_tuples[i], rock_tuples[i + 1])
            # Vertical segment
            if rock_segment[0][0] == rock_segment[1][0]:
                segment_ends = sorted([rock_segment[0][1], rock_segment[1][1]])
                for j in range(segment_ends[0], segment_ends[1] + 1):
                    rock_points.add((rock_segment[0][0], j))
            # Horizontal segment
            elif rock_segment[0][1] == rock_segment[1][1]:
                segment_ends = sorted([rock_segment[0][0], rock_segment[1][0]])
                for j in range(segment_ends[0], segment_ends[1] + 1):
                    rock_points.add((j, rock_segment[0][1]))

# Determine size of cave
cave_vert = set()
cave_hor = set()
for rock_point in rock_points:
    cave_hor.add(rock_point[0])
    cave_vert.add(rock_point[1])
# Use the lowest horizontal coordinate as initial offset
offset = min(cave_hor)
# Initialise cave map
cave_map = []
for i in range(0, max(cave_vert) + 2):
    column = []
    for j in range(offset, max(cave_hor) + 1):
        column.append(".")
    cave_map.append(column)
# Add rock points to cave map
for rock_point in rock_points:
    point_hor = rock_point[0] - offset
    point_vert = rock_point[1]
    cave_map[point_vert][point_hor] = "#"

# Simulate sand
floor, full = simulate_sand(cave_map)
# Print solutions
print("The solution to part 1 is", floor)
print("The solution to part 2 is", full)
