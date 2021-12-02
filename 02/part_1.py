import sys

horizontal_position = 0
depth = 0

for i, line in enumerate(sys.stdin):
    command, command_amount = line.split()
    command_amount = int(command_amount)

    if command == "forward":
        horizontal_position += command_amount
    elif command == "down":
        depth += command_amount
    elif command == "up":
        depth -= command_amount

print(horizontal_position * depth)
