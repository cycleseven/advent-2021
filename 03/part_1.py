import sys

# Keep count of num_ones at each position in `freqs`
# eg. {
#   0: 488,
#   1: 499,
#   2: 497,
#   ...
# }
freqs = {}
total = 0

for line in sys.stdin:
    for j, char in enumerate(line.rstrip()):
        # Only count the occurrences of 1.
        # If a char is not 1 it has to be zero, so no need to track both.
        #
        # (We can always derive num_zeros as [total - num_ones])
        if char == "1":
            freqs[j] = freqs.get(j, 0) + 1

    total += 1

threshold = total * 0.5
epsilon_rate = ""
gamma_rate = ""

for num_ones in freqs.values():
    # If 1 is most common bit...
    if num_ones > threshold:
        gamma_rate += "1"
        epsilon_rate += "0"
    # If 0 is the most common bit
    else:
        gamma_rate += "0"
        epsilon_rate += "1"

# int(str, 2) parses binary number string to an int
print(int(epsilon_rate, 2) * int(gamma_rate, 2))
