"""
`FanFailure <http://community.topcoder.com/stat?c=problem_statement&pm=2235>`__
"""

def solution (capacities, min_cooling):
    capacities = sorted(capacities)

    # calculate MFS
    mfs = 0
    total = sum(capacities)
    for i in range(len(capacities)):
        total -= capacities[i]
        if total >= min_cooling:
            mfs += 1
        else:
            break

    # calculate MFC
    mfc = 0
    total = sum(capacities)
    for i in reversed(range(len(capacities))):
        total -= capacities[i]
        if total >= min_cooling:
            mfc += 1
        else:
            break

    return [mfs, mfc]
