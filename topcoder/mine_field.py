"""
`MineField <http://community.topcoder.com/stat?c=problem_statement&pm=1877>`__
"""

import re

def solution (mines):
    # setup board: 9x9 grid
    board = [list("000000000") for _ in range(9)]

    # mark mines on board
    if len(mines) > 0:
        for pair in re.findall(r'\d+\s*,\s*\d+', mines):
            x, y = [int(c.strip()) for c in pair.split(",")]
            board[x][y] = 'M'

    # calculate adjacency counts
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] != 'M':
                board[x][y] = count(board, x, y)

    # format output
    return ["".join(row) for row in board]

# count number of adjacenct mines
def count (board, x, y):
    count = 0
    if mine(board, x - 1, y - 1): count += 1
    if mine(board, x - 1, y    ): count += 1
    if mine(board, x - 1, y + 1): count += 1
    if mine(board, x,     y - 1): count += 1
    if mine(board, x,     y + 1): count += 1
    if mine(board, x + 1, y - 1): count += 1
    if mine(board, x + 1, y    ): count += 1
    if mine(board, x + 1, y + 1): count += 1
    return str(count)

# determine if mine exists at location
def mine (board, x, y):
    if x < 0:
        return False
    if x > len(board) - 1:
        return False
    if y < 0:
        return False
    if y > len(board[x]) - 1:
        return False
    return board[x][y] == 'M'
