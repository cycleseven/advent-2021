import math
import sys

def triangular_number(n):
    return sum(range(n + 1))

crab_positions = [int(x) for x in sys.stdin.read().rstrip().split(",")]
meanish = math.floor(sum(crab_positions) / len(crab_positions))
print(sum([triangular_number(abs(pos - meanish)) for pos in crab_positions]))
