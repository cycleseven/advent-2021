import sys

fishes = [int(x) for x in sys.stdin.read().rstrip().split(",")]

for i in range(80):
    new_fishes = []

    for j, fish_age in enumerate(fishes):
        if fish_age == 0:
            fishes[j] = 6
            new_fishes.append(8)
        else:
            fishes[j] = fish_age - 1

    fishes = fishes + new_fishes

print(len(fishes))
