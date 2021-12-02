import sys

aim = 0
horizontal_position = 0
depth = 0

for line in sys.stdin:
    command, command_amount = line.split()
    command_amount = int(command_amount)

    if command == "forward":
        horizontal_position += command_amount
        depth += aim * command_amount
    elif command == "down":
        aim += command_amount
    elif command == "up":
        aim -= command_amount

print(horizontal_position * depth)
