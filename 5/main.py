import copy
# Open file
puzzle = open("input.txt", "r")
puzzle_data = puzzle.read()
puzzle_list = puzzle_data.split("\n")
# Separate crates rows from instruction rows
limit = 0
while puzzle_list[limit] != "":
    limit += 1
crate_list = puzzle_list[0:limit]
instruction_list = puzzle_list[limit+1:len(puzzle_list)-1]
# Convert crates rows to stacks
crate_list.reverse()
stacks_number = len(puzzle_list[0])
crate_list.pop(0)
stacks = []
for x in range(1, stacks_number, 4):
    stack = []
    for crate in crate_list:
        if crate[x] != " ":
            stack.append(crate[x])
    stacks.append(stack)
# Process instructions for both parts
part1_stacks = copy.deepcopy(stacks)
part2_stacks = copy.deepcopy(stacks)
for instruction in instruction_list:
    # Parse crate load, input stack, and output stack
    instruction_text = instruction.split(" ")
    crate_load = int(instruction_text[1])
    input_stack = int(instruction_text[3])-1
    output_stack = int(instruction_text[5])-1
    # Move crates according to part 1 instructions (lifo) and part 2 instructions (fifo using crane)
    crane = []
    for x in range(0, crate_load):
        part1_stacks[output_stack].append(part1_stacks[input_stack][-1])
        part1_stacks[input_stack].pop(-1)
        crane.append(part2_stacks[input_stack][-1])
        part2_stacks[input_stack].pop(-1)
    crane.reverse()
    part2_stacks[output_stack].extend(crane)
# Read top crates
part1_top = []
for stack in part1_stacks:
    part1_top.append(stack[-1])
part2_top = []
for stack in part2_stacks:
    part2_top.append(stack[-1])
# Print solution
print("The solution to part 1 is ", *part1_top, sep="")
print("The solution to part 2 is ", *part2_top, sep="")