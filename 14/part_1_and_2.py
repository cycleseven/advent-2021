import collections
import sys

polymer_template = None
pair_insertion_rules = {}

for i, line in enumerate(sys.stdin):
    if i == 0:
        polymer_template = line.rstrip()
    elif i > 1:
        pair, element_to_insert = line.rstrip().split(" -> ")
        pair_insertion_rules[pair] = element_to_insert

element_frequencies = collections.Counter(polymer_template)
pair_frequencies = collections.Counter([
    polymer_template[i:i+2]
    for i in range(len(polymer_template) - 1)
])

for step in range(40):
    new_element_frequencies = collections.Counter()
    new_pair_frequencies = collections.Counter()

    for pair in pair_frequencies:
        count = pair_frequencies[pair]
        new_element = pair_insertion_rules[pair]
        new_pairs = [
            pair[0] + new_element,
            new_element + pair[1]
        ]

        new_element_frequencies.update({
            new_element: count
        })
        new_pair_frequencies.update({
            pair: -count
        })
        new_pair_frequencies.update({
            p: count for p in new_pairs
        })

    element_frequencies.update(new_element_frequencies)
    pair_frequencies.update(new_pair_frequencies)

most_common_element = element_frequencies.most_common()[0]
least_common_element = element_frequencies.most_common()[-1]
print(most_common_element[1] - least_common_element[1])
