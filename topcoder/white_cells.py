"""
`WhiteCells <http://community.topcoder.com/stat?c=problem_statement&pm=8204>`__
"""

def solution (board):
    count      = 0
    white_even = True

    for i in range(len(board)):
        start = 0 if white_even else 1
        for j in range(start, len(board[i]), 2):
            if board[i][j] == 'F':
                count += 1
        white_even = not white_even

    return count
