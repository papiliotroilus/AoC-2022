# Initialise
class Monkey:
    def __init__(self, held_items, operation, test, test_true, test_false, monkey_activity):
        self.held_items = held_items
        self.operation = operation
        self.test = test
        self.test_true = test_true
        self.test_false = test_false
        self.monkey_activity = monkey_activity
rounds_part1 = 20
rounds_part2 = 10000
# Read input
input = open("input.txt", "r")
input_data = input.read()
input_list = input_data.split("\n")
field_list = []
# Turn input to list of monkey data
for line in range(0, len(input_list)):
    if input_list[line][0:6] == 'Monkey':
        # Read items
        current_line = input_list[line + 1]
        items = tuple(int(item) for item in current_line[18:].split(', '))
        # Read operation
        current_line = input_list[line + 2]
        operation_string = current_line[22:]
        # Read test denominator
        current_line = input_list[line + 3]
        denominator = int(current_line[21:])
        # Read receiving monkey for test true
        current_line = input_list[line + 4]
        true_monkey = int(current_line[29:])
        # Read receiving monkey for test false
        current_line = input_list[line + 5]
        false_monkey = int(current_line[30:])
        field_list.append([items, operation_string, denominator, true_monkey, false_monkey])
# Build list of monkey classes from monkey data
monkeys = [Monkey(list(field[0]), field[1], field[2], field[3], field[4], 0) for field in field_list]
# Identify least common multiple for rollover limit
divisors = [monkey.test for monkey in monkeys]
rollover = 1
for divisor in divisors:
    rollover *= divisor
# Define monkeying function
def monkey_around(rounds_number, worry_intensifies):
    for current_round in range(0, rounds_number):
        for this_monkey in range(0, len(monkeys)):
            for item in monkeys[this_monkey].held_items:
                # Inspect item
                old = int(item)
                if worry_intensifies:
                    item = eval('old ' + monkeys[this_monkey].operation)
                else:
                    item = eval('old ' + monkeys[this_monkey].operation) // 3
                # Decrease worry
                item = item % rollover
                monkeys[this_monkey].monkey_activity += 1
                # Test divisibility
                if item % monkeys[this_monkey].test == 0:
                    receiver = monkeys[this_monkey].test_true
                else:
                    receiver = monkeys[this_monkey].test_false
                # Transfer inventory to relevant this_monkey
                receiver_items = monkeys[receiver].held_items
                receiver_items.append(item)
                monkeys[receiver].held_items = receiver_items
            # Wipe current this_monkey inventory
            monkeys[this_monkey].held_items = []
# Solve part 1
monkey_around(rounds_part1, False)
monkey_activities = [monkeys[this_monkey].monkey_activity for this_monkey in range(0, len(monkeys))]
monkey_activities.sort()
monkey_business_part1 = monkey_activities[-1] * monkey_activities[-2]
# Reinitialise for part 2
monkeys = [Monkey(list(field[0]), field[1], field[2], field[3], field[4], 0) for field in field_list]
# Solve part 2
monkey_around(rounds_part2, True)
monkey_activities = [monkeys[this_monkey].monkey_activity for this_monkey in range(0, len(monkeys))]
monkey_activities.sort()
monkey_business_part2 = monkey_activities[-1] * monkey_activities[-2]
# Print solutions
print("The solution to part 1 is", monkey_business_part1)
print("The solution to part 2 is", monkey_business_part2)