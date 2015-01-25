"""
`BinaryCardinality <http://community.topcoder.com/stat?c=problem_statement&pm=1519>`__
"""

def solution (numbers):
    return sorted(sorted(numbers), key=lambda n: cardinality(n))

def cardinality (n):
    count = 0
    for p in reversed(range(0, 21)):
        value = 2 ** p
        if n >= value:
            count += 1
            n     -= value
    return count
