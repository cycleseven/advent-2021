import sys

total = 0

for i, line in enumerate(sys.stdin):
    signals, four_digit_output = [x.split() for x in line.split('|')]

    digit_encodings = {}

    # By sorting the signals by length, we can decode the "easy" signals
    # 1, 7 and 4 first. Then use those to disambiguate the 5-segment
    # and 6-segment digits by using knowledge of how the digit shapes
    # overlap.
    for raw_signal in sorted(signals, key=len):
        signal = frozenset(raw_signal)

        if len(signal) == 2:
            digit_encodings[1] = signal
        elif len(signal) == 3:
            digit_encodings[7] = signal
        elif len(signal) == 4:
            digit_encodings[4] = signal

        # We need to differentiate the 5-segment digits using some tricks.
        # The 5-segment digits are 2, 3, and 5.
        elif len(signal) == 5:
            # Trick #1: find "3".
            #
            # The "3" shape is the only 5-segment digit that contains
            # the "1" shape as a subset.
            if digit_encodings[1].issubset(signal):
                digit_encodings[3] = signal
            # Trick #2: find "5".
            #
            # The "4" digit uses segments b + d. You can narrow down the possible
            # wires for those segments by subtracting the "1" shape from the "4" shape,
            # leaving two possible wires.
            #
            # The "5" digit is the only digit that also uses *both* of those wires.
            elif (digit_encodings[4] - digit_encodings[1]).issubset(signal):
                digit_encodings[5] = signal
            # The other possible 5-segment digit is "2", soooo...
            else:
                digit_encodings[2] = signal

        # Similarly, let's use some tricks to disambiguate the 6-segment digits.
        # The 6-segment digits are 0, 6 and 9.
        elif len(signal) == 6:
            # Trick #1: find "9".
            #
            # The "4" shape is a subset of the "9" shape, unlike "0" (which lacks
            # segment d) and "6" (which lacks segment c).
            if digit_encodings[4].issubset(signal):
                digit_encodings[9] = signal
            # Trick #2: find "0".
            #
            # "0" is the only shape which has "7" as a sub-shape but not "4".
            # Since we reached this condition, we already know 4 is not
            # a subset of this signal's shape. So...
            elif digit_encodings[7].issubset(signal):
                digit_encodings[0] = signal
            # The other possible 6-segment digit is "6"
            else:
                digit_encodings[6] = signal
        elif len(signal) == 7:
            digit_encodings[8] = signal

    # Invert the map so we can easily look up the signal for each digit
    signal_to_digit = { signal: digit for digit, signal in digit_encodings.items() }

    output_number = 0
    four_digit_output.reverse()
    for i, raw_output_signal in enumerate(four_digit_output):
        output_signal = frozenset(raw_output_signal)
        digit = signal_to_digit[output_signal]
        output_number += 10 ** i * digit

    total += output_number

print(total)
