"""
`DietPlan <http://community.topcoder.com/stat?c=problem_statement&pm=8222>`__
"""

def solution (diet, breakfast, lunch):
    rem = set()
    for d in diet:
        rem.add(d)

    for b in breakfast:
        if b not in rem:
            return "CHEATER"
        rem.remove(b)

    for l in lunch:
        if l not in rem:
            return "CHEATER"
        rem.remove(l)

    return "".join(sorted(list(rem)))
