import collections
import pprint
import sys

## Utils

def raise_bad_line_error(line):
    print("Bad line encountered")
    pprint.pprint(line)
    raise ValueError("Line is neither horizontal, vertical or diagonal")

def get_line_range_in_dimension(line, dim):
    # dim is "x" or "y"
    range_start = line[0][dim]

    # If the second coord defining the line has a smaller x/y value,
    # then the range is _decrementing_. Figure out the range_end and
    # step accordingly. The range_end is always one more step beyond,
    # the final value, and step is -1 if decrementing.
    if line[0][dim] > line[1][dim]:
        range_end = line[1][dim] - 1
        step = -1
    else:
        range_end = line[1][dim] + 1
        step = 1

    return range(range_start, range_end, step)

def is_vertical_line(line):
    return line[0]['x'] == line[1]['x']

def is_horizontal_line(line):
    return line[0]['y'] == line[1]['y']

def is_diagonal_line(line):
    return abs(line[0]['y'] - line[1]['y']) == abs(line[0]['x'] - line[1]['x'])

def get_vertical_extremes(line):
    min_y = min(line[0]['y'], line[1]['y'])
    max_y = max(line[0]['y'], line[1]['y'])

    return min_y, max_y

def get_horizontal_extremes(line):
    min_x = min(line[0]['x'], line[1]['x'])
    max_x = max(line[0]['x'], line[1]['x'])

    return min_x, max_x

"""Given a line (defined by its endpoints), return the full array of points that form the line.

eg. [{ 'x': 1, 'y': 1 }, { 'x': 1, 'y': 3 }]
    => [ { 'x': 1, 'y': 1 }, { 'x': 1, 'y': 2 }, { 'x': 1, 'y': 3 } ]
"""
def line_to_points(line):
    if is_vertical_line(line):
        min_y, max_y = get_vertical_extremes(line)

        return [
            { "x": line[0]['x'], "y": y }
            for y in range(min_y, max_y + 1)
        ]
    elif is_horizontal_line(line):
        min_x, max_x = get_horizontal_extremes(line)

        return [
            { "x": x, "y": line[0]['y'] }
            for x in range(min_x, max_x + 1)
        ]
    elif is_diagonal_line(line):
        x_range = get_line_range_in_dimension(line, 'x')
        y_range = get_line_range_in_dimension(line, 'y')

        points = [
            { "x": x, "y": y }
            for x, y in zip(x_range, y_range)
        ]
        return points

    raise_bad_line_error(line)

def point_to_key(point):
    return f"{point['x']},{point['y']}"

## Input parsing

lines = [
    [
        {
            "x": int(coord.split(',')[0]),
            "y": int(coord.split(',')[1])
        }
        for coord
        in input_line.rstrip().split(' -> ')
    ]
    for input_line in sys.stdin.readlines()
]

## The algorithm
#
# (See part_1.py for an explanation)

previous_vent_points = {}
num_overlapping_points = 0

for line in lines:
    line_points = line_to_points(line)

    for point in line_points:
        key = point_to_key(point)

        if key in previous_vent_points:
            if not previous_vent_points[key]:
                previous_vent_points[key] = True
                num_overlapping_points += 1

            continue

        previous_vent_points[key] = False

print(num_overlapping_points)
