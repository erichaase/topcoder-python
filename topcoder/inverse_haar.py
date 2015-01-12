"""
`InverseHaar1D <http://community.topcoder.com/stat?c=problem_statement&pm=5896>`__
"""

def solution (t, l):
    if (l == 1):
        # level-1 untransformation
        i = len(t) / 2
        sums, diffs = t[:i], t[i:]

        ut = []
        for j in range(len(sums)):
            # a + b = s,       a - b = d
            # a = (s + d) / 2, b = (s - d) / 2
            s, d = sums[j],     diffs[j]
            a, b = (s + d) / 2, (s - d) / 2
            ut.extend([a, b])
        return ut
    else:
        # level-x untransformation
        i = len(t) / (2 ** (l - 1))
        head, tail = t[:i], t[i:]
        ut = solution(head, 1) + tail
        return solution(ut, l - 1)
