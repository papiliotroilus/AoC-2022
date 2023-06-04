# Open file
puzzle = open("input.txt", "r")
puzzle_data = puzzle.read()
puzzle_list = puzzle_data.split("\n")
puzzle_list.pop(-1)
# Solve puzzle
visible = len(puzzle_list)*2+len(puzzle_list[0])*2-4
highest_scenic = 0
for row in range(1, len(puzzle_list)-1):
    for column in range(1, len(puzzle_list[row])-1):
        tree = int((puzzle_list[row][column]))
        west = []
        for westing in range(column-1, -1, -1):
            west.append(int(puzzle_list[row][westing]))
            if int(puzzle_list[row][westing]) >= tree:
                break
        west_max = max(west, default=-1)
        west_count = len(west)
        east = []
        for easting in range(column+1, len(puzzle_list[row])):
            east.append(int(puzzle_list[row][easting]))
            if int(puzzle_list[row][easting]) >= tree:
                break
        east_max = max(east, default=-1)
        east_count = len(east)
        north = []
        for northing in range(row-1, -1, -1):
            north.append(int(puzzle_list[northing][column]))
            if int(puzzle_list[northing][column]) >= tree:
                break
        north_max = max(north, default=-1)
        north_count = len(north)
        south = []
        for southing in range(row+1, len(puzzle_list)):
            south.append(int(puzzle_list[southing][column]))
            if int(puzzle_list[southing][column]) >= tree:
                break
        south_max = max(south, default=-1)
        south_count = len(south)
        if east_max < tree or west_max < tree or north_max < tree or south_max < tree:
            visible += 1
        scenic_score = west_count * east_count * north_count * south_count
        if highest_scenic < scenic_score:
            highest_scenic = scenic_score
# Print solution
print("The solution to part 1 is ", visible)
print("The solution to part 2 is ", highest_scenic)