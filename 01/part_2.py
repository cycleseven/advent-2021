import sys

if __name__ == "__main__":
    num_increases = 0
    sliding_window = []
    prev_sum = None
    total = 0

    for i, line in enumerate(sys.stdin):
        current = int(line.rstrip())

        if len(sliding_window) < 3:
            sliding_window.append(current)

            if (len(sliding_window)) == 3:
                prev_sum = sum(sliding_window)

            continue

        sliding_window.pop(0)
        sliding_window.append(current)
        current_sum = sum(sliding_window)

        if prev_sum < current_sum:
            num_increases += 1

        total += 1
        prev_sum = current_sum

    print(num_increases)
