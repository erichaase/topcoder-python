"""
`EqualizeStrings <http://community.topcoder.com/stat?c=problem_statement&pm=10933>`__
"""

def solution (s, t):
    out = ""
    for i in range(len(s)):
        x = s[i]
        y = t[i]
        diff = abs(ord(x) - ord(y))
        if diff < 26 / 2:
            # values are close by, use minimum
            out += min([x, y])
        else:
            # values are far, wrapping always uses 'a'
            out += 'a'
    return out
