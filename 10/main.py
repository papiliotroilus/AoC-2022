# Initialise CPU
register = 1
cycle = 0
strengths = []
line = []
display = []
def cycle_check():
    if cycle in [20, 60, 100, 140, 180, 220]:
        strengths.append(cycle * register)
    line.append(' ')
    if register - 1 == len(line) - 1 or register == len(line) - 1 or register + 1 == len(line) - 1:
        line[-1] = '█'
    if cycle % 40 == 0:
        line_string = ' '.join(line)
        display.append(line_string)
        line.clear()
# Read input
with open('input.txt') as puzzle:
    for puzzle_line in puzzle:
        puzzle_line = puzzle_line.rstrip('\r\n')
        if puzzle_line == 'noop':
            cycle += 1
            cycle_check()
        elif puzzle_line[0:4] == 'addx':
            cycle += 1
            cycle_check()
            cycle += 1
            cycle_check()
            register += int(puzzle_line[5:len(puzzle_line) + 1])
# Print solutions
print("The solution to part 1 is", sum(strengths))
print("The solution to part 2 is")
print(*display, sep="\n")