"""
`Genetics <http://community.topcoder.com/stat?c=problem_statement&pm=2973>`__
"""

def solution (g1, g2, dom):
    out = ""
    # iterate over each pair of chars and append result
    for i in range(len(dom)):
        a, b, d = g1[i], g2[i], dom[i]
        if a == b:
            out += a
        else:
            if d == 'D':
                out += a.upper()
            else:
                out += a.lower()
    return out
