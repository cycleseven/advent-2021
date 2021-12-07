import math
import sys

crab_positions = [int(x) for x in sys.stdin.read().rstrip().split(",")]
medianish = sorted(crab_positions)[math.floor(len(crab_positions) * 0.5)]
print(sum([abs(pos - medianish) for pos in crab_positions]))
