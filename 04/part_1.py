import sys
import pprint

lines = sys.stdin.readlines()
bingo_numbers = [int(x) for x in lines[0].rstrip().split(',')]

# After these parsing steps, bingo_boards is a list of 5x5 2D arrays of ints eg.
#
# [
#
#  [[78, 27, 82, 68, 20],
#   [14, 2, 34, 51, 7],
#   [58, 57, 99, 37, 81],
#   [9, 4, 0, 76, 45],
#   [67, 69, 70, 17, 23]],
#
#  [[38, 60, 62, 34, 41],
#   [39, 58, 91, 45, 10],
#   [66, 74, 94, 50, 17],
#   [68, 27, 75, 97, 49],
#   [36, 64, 5, 98, 15]],
#
#  ...
#
# ]
flat_bingo_boards = [[int(x) for x in line.rstrip().split()] for line in lines[1:] if line != "\n"]
bingo_boards = [flat_bingo_boards[i:i + 5] for i in range(0, len(flat_bingo_boards), 5)]

# Keep track of "marked" board positions via another list of 5x5 2D arrays
# Every position starts as False eg.
#
# [
#
#  [[False, False, False, False, False],
#   [False, False, False, False, False],
#   [False, False, False, False, False],
#   [False, False, False, False, False],
#   [False, False, False, False, False]],
#
#  [[False, False, False, False, False],
#   [False, False, False, False, False],
#   [False, False, False, False, False],
#   [False, False, False, False, False],
#   [False, False, False, False, False]],
#
#   ...
#
# ]
marked_bingo_board_positions = [
    [[False for _ in range(5)] for _ in range(5)]
    for _ in range(len(bingo_boards))
]

def find_winning_bingo_board():
    for bingo_number in bingo_numbers:
        for i, bingo_board in enumerate(bingo_boards):

            # Optimistically assume each row/col is a winning one.
            #
            # If we find out while iterating that any number doesn't match a called bingo number,
            # we'll invalidate this assumption.
            #
            # A number matches if we already marked it previously, or if it matches the current
            # bingo_number.
            #
            # If we iterate all the way through the board and a row/col is still "promising",
            # every number in that col/row has been called and the game is won
            promising_cols = [True for _ in range(5)]
            promising_rows = [True for _ in range(5)]

            for row in range(5):
                for col in range(5):
                    if marked_bingo_board_positions[i][row][col]:
                        continue

                    if bingo_board[row][col] == bingo_number:
                        marked_bingo_board_positions[i][row][col] = True
                        continue

                    # The number isn't matching any bingo numbers yet. So the col + row
                    # that this number lies in are no longer promising.
                    promising_rows[row] = False
                    promising_cols[col] = False

            if any(promising_cols) or any(promising_rows):
                return bingo_board, i, bingo_number

winning_bingo_board, winning_index, last_number_called = find_winning_bingo_board()
print(winning_bingo_board, winning_index, last_number_called)

sum_of_unmarked_numbers = 0
for row in range(5):
    for col in range(5):
        if not marked_bingo_board_positions[winning_index][row][col]:
            sum_of_unmarked_numbers += winning_bingo_board[row][col]

print(last_number_called * sum_of_unmarked_numbers)

