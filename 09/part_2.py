import math
import sys

heightmap = [
    [int(datum) for datum in list(line.rstrip())]
    for line in sys.stdin.readlines()
]
map_height = len(heightmap)
map_width = len(heightmap[0])

# Tracks previously explored basin locations
basinmap = [
    [False for _ in row]
    for row in heightmap
]

# Tracks the 3 largest basins encountered so far
largest_basin_sizes = []

adjacent_deltas = [
    [0, -1],    # left
    [-1, 0],    # up
    [0, 1],     # right
    [1, 0],     # down
]

def explore_basin(initial_i, initial_j):
    basin_size = 0
    next_locations_to_explore = [(initial_i, initial_j)]
    basinmap[initial_i][initial_j] = True

    while len(next_locations_to_explore) > 0:
        i, j = next_locations_to_explore.pop(0)
        basin_size += 1

        adjacent_locations = []
        for delta_i, delta_j in adjacent_deltas:
            adj_i, adj_j = (i + delta_i, j + delta_j)
            adjacent_coord_is_in_range = (
                adj_i >= 0 and
                adj_i < map_height and
                adj_j >= 0 and
                adj_j < map_width
            )

            if not adjacent_coord_is_in_range:
                continue

            adjacent_coord_is_new_basin_coord = (
                not basinmap[adj_i][adj_j] and
                heightmap[adj_i][adj_j] != 9
            )

            if adjacent_coord_is_new_basin_coord:
                adjacent_locations.append((adj_i, adj_j))
                basinmap[adj_i][adj_j] = True

        next_locations_to_explore += adjacent_locations

    return basin_size

for i, row in enumerate(heightmap):
    for j, height in enumerate(row):
        if height != 9 and not basinmap[i][j]:
            basin_size = explore_basin(i, j)

            if len(largest_basin_sizes) < 3:
                largest_basin_sizes.append(basin_size)
                largest_basin_sizes.sort()
            elif basin_size > largest_basin_sizes[0]:
                largest_basin_sizes.pop(0)
                largest_basin_sizes.append(basin_size)
                largest_basin_sizes.sort()

print(math.prod(largest_basin_sizes))
