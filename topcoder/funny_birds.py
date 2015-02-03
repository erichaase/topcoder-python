"""
`FunnyBirds <http://community.topcoder.com/stat?c=problem_statement&pm=9769>`__
"""

def solution (n):
    k = 1
    t = 0

    while n:
        if n < k:
            k = 1
        n -= k
        t += 1
        k += 1

    return t
