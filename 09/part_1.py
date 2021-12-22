import sys

heightmap = [
    [int(datum) for datum in list(line.rstrip())]
    for line in sys.stdin.readlines()
]
map_height = len(heightmap)
map_width = len(heightmap[0])

total_risk_level = 0

def get_adjacent_heights(i1, j1):
    adjacent_coords = [
        [i1, j1 - 1],   # left
        [i1 - 1, j1],   # up
        [i1, j1 + 1],   # right
        [i1 + 1, j1],   # down
    ]

    return [
        heightmap[i2][j2]
        for i2, j2 in adjacent_coords
        if i2 >= 0 and i2 < map_height and j2 >= 0 and j2 < map_width
    ]

for i, row in enumerate(heightmap):
    for j, height in enumerate(row):
        if all([height < adjacent_height for adjacent_height in get_adjacent_heights(i, j)]):
            total_risk_level += 1 + height

print(total_risk_level)
