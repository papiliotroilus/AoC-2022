def compare(left, right):
    # Test if both items are integers and test them if so
    if type(left) == int and type(right) == int:
        if left > right:
            return 'left bigger'
        elif left < right:
            return 'right bigger'
        else:
            return 'equal'
    # Convert integers to lists
    if type(left) == int:
        left = [left]
    if type(right) == int:
        right = [right]
    # Recurse through comparing list items
    recurse = 'equal'
    while recurse == 'equal':
        # Manage empty lists
        if left == [] and right != []:
            return 'right bigger'
        elif right == [] and left != []:
            return 'left bigger'
        elif left == [] and right == []:
            return 'equal'
        # Manage non-empty lists
        recurse = compare(left[0], right[0])
        if recurse == 'right bigger':
            return 'right bigger'
        elif recurse == 'left bigger':
            return 'left bigger'
        elif recurse == 'equal':
            left.pop(0)
            right.pop(0)


# Initialise
pairs = []
index = 0
index_sum = 0
part21 = []
part22 = []
# Solve part 1
with open('input.txt') as puzzle:
    for puzzle_line in puzzle:
        puzzle_line = puzzle_line.rstrip('\r\n')
        # Identify packet and add to pair
        if len(puzzle_line) != 0:
            pairs.append(eval(puzzle_line))
            part21.append(eval(puzzle_line))
            part22.append(eval(puzzle_line))
        # Process packet pair
        else:
            index += 1
            verdict = 'equal'
            while verdict == 'equal':
                verdict = compare(pairs[0], pairs[1])
                if verdict == 'right bigger':
                    index_sum += index
                elif verdict == 'equal':
                    pairs[0].pop(0)
                    pairs[1].pop(0)
            pairs = []
            verdict = 'equal'
# Solve part 2
# Find first separator index
index1 = 1
for packet in part21:
    separator1 = [[2]]
    verdict = 'equal'
    while verdict == 'equal':
        verdict = compare(packet, separator1)
        if verdict == 'right bigger':
            index1 += 1
        elif verdict == 'equal':
            separator1.pop(0)
            packet.pop(0)
# Find second separator index
index2 = 2
for packet in part22:
    separator2 = [[6]]
    verdict = 'equal'
    while verdict == 'equal':
        verdict = compare(packet, separator2)
        if verdict == 'right bigger':
            index2 += 1
        elif verdict == 'equal':
            separator2.pop(0)
            packet.pop(0)
# Print solutions
print("The solution to part 1 is", index_sum)
print("The solution to part 2 is", index1 * index2)
