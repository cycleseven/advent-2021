import collections
import pprint
import sys

## Utils

def raise_bad_line_error(line):
    print("Bad line encountered")
    pprint.pprint(line)
    raise ValueError("Line is neither horizontal nor vertical")

def is_vertical_line(line):
    return line[0]['x'] == line[1]['x']

def is_horizontal_line(line):
    return line[0]['y'] == line[1]['y']

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

    raise_bad_line_error(line)

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

# The idea is to break each line into the points that make it up. Then, find out if any of those
# points match up with a point that's already been encountered _once_ (and no more than once,
# we don't want to double-count points with an overlap).
#
# This is mainly achieved by tracking previous lines via the previous_vent_points data structure.
# It's a nested dict, where the root keys are x-coords of previously encountered points,
# the nested keys are the y-coords, and the values are True/False.
#
# For example, if we encounter these points: [1,1], [1,2], [1,3], previous_vent_points looks like
# this:
#
# {
#   "1": {
#     "1": False,
#     "2": False,
#     "3": False,
#   }
# }
#
# If later on, the point [1,2] is found to overlap another line, this is tracked with a "True"
# value:
#
# {
#   "1": {
#     "1": False,
#     "2": True,
#     "3": False,
#   }
# }
#
# This allows O(1) lookup of whether any point has (a) appeared in a previous line, and (b) has
# appeared in a previous overlap.

previous_vent_points = {}
num_overlapping_points = 0

for line in lines:
    if not (is_horizontal_line(line) or is_vertical_line(line)):
        continue

    line_points = line_to_points(line)

    for point in line_points:
        if point['x'] in previous_vent_points and point['y'] in previous_vent_points[point['x']]:
            # We know we've seen this point before. Was it already involved in an overlap?
            # If not, this is a new overlapping point, so increment num_overlapping_points.
            if not previous_vent_points[point['x']][point['y']]:
                # Mark the vent point as "used", we already know it's an overlapping point and
                # we don't count it again in later iterations.
                previous_vent_points[point['x']][point['y']] = True
                num_overlapping_points += 1

            continue

        # This vent point is one we haven't seen before. Track it in previous_vent_points.
        # Initially set the value to False (since the vent point hasn't yet been
        # detected as an overlapping point).
        try:
            previous_vent_points[point['x']].update({
                point['y']: False
            })
        except KeyError:
            previous_vent_points[point['x']] = { point['y']: False }

print(num_overlapping_points)
