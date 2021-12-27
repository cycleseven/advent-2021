import sys

char_pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

illegal_character_scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

syntax_error_score = 0

for line in sys.stdin:
    chunk_stack = []
    illegal_char = None

    for char in line:
        if char in char_pairs.keys():
            chunk_stack.append(char_pairs[char])
        elif char in char_pairs.values():
            expected_char = chunk_stack.pop()

            if char != expected_char:
                illegal_char = char
                break

    if illegal_char is not None:
        syntax_error_score += illegal_character_scores[illegal_char]

print(syntax_error_score)
