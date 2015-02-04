"""
`RevealTriangle <http://community.topcoder.com/stat?c=problem_statement&pm=8215>`__
"""

import re

def solution (triangle):
    # iterate from bottom to top of triangle, solving each line
    for i in reversed(range(0, len(triangle) - 1)):
        triangle[i] = solve_line(triangle[i], triangle[i+1])
    return triangle

def solve_line (current, below):
    line    = list(current)
    imiddle = re.search(r'\d', current).start()

    # process left of known number
    for i in reversed(range(0, imiddle)):
        line[i] = solve_char(line[i+1], below[i])

    # process right of known number
    for i in range(imiddle + 1, len(line)):
        line[i] = solve_char(line[i-1], below[i-1])

    return "".join(line)

def solve_char (lr, below):
    lr, below = int(lr), int(below)

    if lr > below:
        return str(below + 10 - lr)
    else:
        return str(below - lr)
