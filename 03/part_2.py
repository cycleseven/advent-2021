import sys

possible_oxygen_generator_ratings = []
possible_co2_scrubber_ratings = []

for line in sys.stdin:
    binary_str = line.rstrip()
    possible_oxygen_generator_ratings.append(binary_str)
    possible_co2_scrubber_ratings.append(binary_str)

"""Given a list of binary strings, bin them into two categories
   depending on whether there's a 0 or a 1 at the given index."""
def categorise_possibilities_by_bit(possibilities, current_index):
    by_bit = {
        0: [],
        1: [],
    }

    for entry in possibilities:
        if entry[current_index] == "0":
            by_bit[0].append(entry)
        else:
            by_bit[1].append(entry)

    return by_bit

for i in range(len(possible_oxygen_generator_ratings[0])):
    if len(possible_oxygen_generator_ratings) == 1:
        break

    by_bit = categorise_possibilities_by_bit(possible_oxygen_generator_ratings, i)

    # Update the list of possible_oxygen_generator_ratings to be those with
    # the "winning" bit at the current position i.
    # In case of ties, pick by_bit[1]
    if (len(by_bit[0]) > len(by_bit[1])):
        possible_oxygen_generator_ratings = by_bit[0]
    else:
        possible_oxygen_generator_ratings = by_bit[1]

for i in range(len(possible_co2_scrubber_ratings[0])):
    if len(possible_co2_scrubber_ratings) == 1:
        break

    by_bit = categorise_possibilities_by_bit(possible_co2_scrubber_ratings, i)

    # Update the list of possible_co2_scrubber_ratings to be those with
    # the least common bit at the current position i.
    # In case of ties, pick by_bit[0]
    if (len(by_bit[0]) > len(by_bit[1])):
        possible_co2_scrubber_ratings = by_bit[1]
    else:
        possible_co2_scrubber_ratings = by_bit[0]

print(int(possible_co2_scrubber_ratings[0], 2) * int(possible_oxygen_generator_ratings[0], 2))
