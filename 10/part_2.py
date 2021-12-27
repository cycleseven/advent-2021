import math
import sys

char_pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

char_scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

autocompletion_scores = []

for line in sys.stdin:
    chunk_stack = []
    is_corrupt = False

    for char in line:
        if char in char_pairs.keys():
            chunk_stack.append(char_pairs[char])
        elif char in char_pairs.values():
            expected_char = chunk_stack.pop()

            if char != expected_char:
                # This line is corrupted, discard it
                is_corrupt = True
                break

    if is_corrupt:
        continue

    autocompletion_score = 0
    for completion_char in reversed(chunk_stack):
        autocompletion_score *= 5
        autocompletion_score += char_scores[completion_char]

    autocompletion_scores.append(autocompletion_score)

autocompletion_scores.sort()
midpoint = len(autocompletion_scores) * 0.5
print(autocompletion_scores[int(midpoint)])
