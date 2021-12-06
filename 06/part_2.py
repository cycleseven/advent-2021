import math
import sys

fishes = [int(x) for x in sys.stdin.read().rstrip().split(",")]
fish_freqs = {}

for i in range(9):
    fish_freqs[i] = len([t for t in fishes if t == i])

for i in range(256):
    new_freqs = {}

    for j in range(9):
        if j == 6:
            new_freqs[j] = fish_freqs[7] + fish_freqs[0]
        elif j == 8:
            new_freqs[j] = fish_freqs[0]
        else:
            new_freqs[j] = fish_freqs[j + 1]

    fish_freqs = new_freqs

print(sum(fish_freqs.values()))
