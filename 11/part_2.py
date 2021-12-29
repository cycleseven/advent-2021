import sys

octopuses = [
    [int(x) for x in line.rstrip()]
    for line in sys.stdin.readlines()
]

step = 0

while True:
    step += 1
    flashed_dumbos = {}
    dumbos_to_flash = []

    for i, row in enumerate(octopuses):
        for j, dumbo in enumerate(row):
            octopuses[i][j] += 1

            if octopuses[i][j] > 9:
                flashed_dumbos[(i, j)] = True
                dumbos_to_flash.append((i, j))

    while len(dumbos_to_flash) > 0:
        centre = dumbos_to_flash.pop(0)

        for i in range(centre[0] - 1, centre[0] + 2):
            for j in range(centre[1] - 1, centre[1] + 2):
                is_centre = i == centre[0] and j == centre[1]
                is_out_of_range = i < 0 or i > 9 or j < 0 or j > 9
                already_flashed = (i, j) in flashed_dumbos

                if is_centre or is_out_of_range or already_flashed:
                    continue

                octopuses[i][j] += 1

                if octopuses[i][j] > 9:
                    flashed_dumbos[(i, j)] = True
                    dumbos_to_flash.append((i, j))

    if len(flashed_dumbos) == 100:
        print(step)
        sys.exit(0)

    for i, j in flashed_dumbos:
        octopuses[i][j] = 0
