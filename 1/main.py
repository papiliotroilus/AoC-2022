puzzleinput = open("input.txt", "r")
puzzleinput_data = puzzleinput.read()
rawlist = puzzleinput_data.split("\n")
newlist = []
sublist = []
for element in rawlist:
    if element != "":
        sublist.append(int(element))
    else:
        newlist.append(sublist)
        sublist = []
totallist = []
for sublist in newlist:
    total = sum(sublist)
    totallist.append(total)
totallist.sort()
print("The solution to part 1 is", totallist[-1])
print("The solution to part 2 is", totallist[-1]+totallist[-2]+totallist[-3])
