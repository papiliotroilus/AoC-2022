puzzleinput = open("input.txt", "r")
puzzleinput_data = puzzleinput.read()
rawlist = puzzleinput_data.split("\n")
rawlist.pop(-1)
newlist = []
for rucksack in rawlist:
    first = rucksack[0:len(rucksack)//2]
    second = rucksack[len(rucksack)//2:len(rucksack)]
    newlist.append([first,second])
repeats = []
for rucksack in newlist:
    firstset=set(rucksack[0])
    secondset=set(rucksack[1])
    repeats.append(''.join(firstset.intersection(secondset)))
prioritysum=0
for item in repeats:
    if item.isupper():
        prioritysum=prioritysum+ord(item)-64+26
    else:
        prioritysum=prioritysum+ord(item)-96
badges = []
for x in range(0,len(rawlist)//3):
    badges.append(str((set(rawlist[x*3]) & set(rawlist[x*3+1]) & set(rawlist[x*3+2])))[2])
badgeprioritysum=0
for badge in badges:
    if badge.isupper():
        badgeprioritysum=badgeprioritysum+ord(badge)-64+26
    elif badge.islower():
        badgeprioritysum=badgeprioritysum+ord(badge)-96
print("The solution to part 1 is",prioritysum)
print("The solution to part 1 is",badgeprioritysum)