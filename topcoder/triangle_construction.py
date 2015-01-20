"""
`TriangleConstruction <http://community.topcoder.com/stat?c=problem_statement&pm=7523>`__
"""

import itertools

def solution (lengths):
    max = -1
    # iterate through all of the diff combinations of sticks
    for triangle in itertools.combinations(lengths, 3):
        x, y, z = sorted(triangle)
        if not x + y > z:
            continue
        s = sum(triangle)
        if s > max:
            max = s
    return max
