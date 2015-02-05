"""
`ColorfulRabbits <http://community.topcoder.com/stat?c=problem_statement&pm=11327>`__
"""

import math

def solution (replies):
    # track count of groups of colors
    h = {}
    for c in replies:
        if c+1 in h:
            h[c+1] += 1
        else:
            h[c+1] = 1

    # calculate n assuming minimal groups
    n = 0
    for s, c in h.items():
        n += s * int(math.ceil(float(c) / s))
    return n
