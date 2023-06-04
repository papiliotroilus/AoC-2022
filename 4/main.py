puzzleinput = open("input.txt", "r")
puzzleinput_data = puzzleinput.read()
rawlist = puzzleinput_data.split("\n")
rawlist.pop(-1)
pairlist = []
for pair in rawlist:
    splitpair = pair.split(",")
    pairlist.append(splitpair)
for pairs in pairlist:
    firstpair = pairs[0].split("-")
    secondpair = pairs[1].split("-")
    pairs[0] = firstpair
    pairs[1] = second
    pair
intervallist = []
for pairs in pairlist:
    firstrange = range(int(pairs[0][0]), int(pairs[0][1]) + 1, 1)
    secondrange = range(int(pairs[1][0]), int(pairs[1][1]) + 1, 1)
    intervallist.append((list(firstrange), list(secondrange)))
containments = 0
intersections = 0
for pair in intervallist:
    if all(sector in pair[0] for sector in pair[1]) or all(sector in pair[1] for sector in pair[0]):
        containments += 1
    if any(sector in pair[0] for sector in pair[1]) or any(sector in pair[1] for sector in pair[0]):
        intersections += 1
print("The solution to part 1 is", containments)
print("The solution to part 2 is", intersections)
