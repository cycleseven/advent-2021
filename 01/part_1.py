import sys

if __name__ == "__main__":
    num_increases = 0
    prev = None
    total = 0

    for line in sys.stdin:
        current = int(line.rstrip())

        if prev is None:
            prev = current
            continue

        if prev < current:
            num_increases += 1

        total += 1
        prev = current

    print(num_increases)
