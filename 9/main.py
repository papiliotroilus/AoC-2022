# Initialise rope
head = [0, 0]
tail = []
segment_number = 9
for segment in range(0, segment_number):
    tail.append([0, 0])
visited_first = []
visited_last = []
# Read input
with open('input.txt') as puzzle:
    for puzzle_line in puzzle:
        puzzle_line = puzzle_line.rstrip('\r\n')
        direction = puzzle_line[0]
        distance = int(puzzle_line[2:len(puzzle_line)])
        while distance > 0:
            # Move head
            if direction == "L":
                head[0] -= 1
            elif direction == "R":
                head[0] += 1
            elif direction == "U":
                head[1] += 1
            elif direction == "D":
                head[1] -= 1
            # Move tail
            def rope_physics(seg_1, seg_2):
                if abs(seg_1[0] - seg_2[0]) == 2 and seg_1[1] == seg_2[1]:
                    seg_2[0] += int((seg_1[0]-seg_2[0]) / 2)
                elif abs(seg_1[1] - seg_2[1]) == 2 and seg_1[0] == seg_2[0]:
                    seg_2[1] += int((seg_1[1]-seg_2[1]) / 2)
                elif abs(seg_1[0] - seg_2[0]) == 2 and abs(seg_1[1] - seg_2[1]) == 1:
                    seg_2[0] += int((seg_1[0]-seg_2[0]) / 2)
                    seg_2[1] += int(seg_1[1] - seg_2[1])
                elif abs(seg_1[1] - seg_2[1]) == 2 and abs(seg_1[0] - seg_2[0]) == 1:
                    seg_2[1] += int((seg_1[1]-seg_2[1]) / 2)
                    seg_2[0] += int(seg_1[0] - seg_2[0])
                elif abs(seg_1[0] - seg_2[0]) == 2 and abs(seg_1[1] - seg_2[1]) == 2:
                    seg_2[0] += int((seg_1[0] - seg_2[0]) / 2)
                    seg_2[1] += int((seg_1[1] - seg_2[1]) / 2)
            rope_physics(head, tail[0])
            for segment in range(0, len(tail)-1):
                rope_physics(tail[segment], tail[segment+1])
            distance -= 1
            visited_first.append((str(tail[0][0])+'/'+str(tail[0][1])))
            visited_last.append((str(tail[-1][0])+'/'+str(tail[-1][1])))
# Print solutions
print("The solution to part 1 is", len(set(visited_first)))
print("The solution to part 2 is", len(set(visited_last)))