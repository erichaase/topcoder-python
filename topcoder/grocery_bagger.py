"""
`GroceryBagger <http://community.topcoder.com/stat?c=problem_statement&pm=3450>`__
"""

import math

def solution (strength, items):
    h = {}
    for item in items:
        if item in h:
            h[item] += 1
        else:
            h[item] = 1

    bags = 0
    for count in h.values():
        bags += int(math.ceil(float(count) / strength))
    return bags
