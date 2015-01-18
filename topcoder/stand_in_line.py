"""
`StandInLine <http://community.topcoder.com/stat?c=problem_statement&pm=6631>`__
"""

def solution (left):
    out = [None for _ in range(len(left))]

    # iterate through left data structure
    for i, n in enumerate(left):
        h, taller = i + 1, 0

        # place current in final out position
        for j, v in enumerate(out):
            if not v:
                if taller == n:
                    out[j] = h
                    break
                taller += 1

    return out
