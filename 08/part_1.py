import sys

total_unique_digits = 0

segment_count_for_digit = {
    1: 2,
    4: 4,
    7: 3,
    8: 7,
}

possible_digits_by_segment_count = {}
for digit, segment_count in segment_count_for_digit.items():
    possible_digits_by_segment_count \
        .setdefault(segment_count, set()) \
        .add(digit)

for line in sys.stdin:
    signal_examples, four_digit_output = [x.split() for x in line.split('|')]

    for digit in four_digit_output:
        num_segments = len(digit)
        if num_segments in possible_digits_by_segment_count:
            total_unique_digits += 1

print(total_unique_digits)
