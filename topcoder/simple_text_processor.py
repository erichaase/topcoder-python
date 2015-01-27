"""
`SimpleTextProcessor <http://community.topcoder.com/stat?c=problem_statement&pm=7805>`__
"""

def solution (words):
    left  = words[0:len(words)/2]
    right = words[len(words)/2:]

    max_left  = max([len(s) for s in left])
    max_right = max([len(s) for s in right])

    out = []
    for i in range(len(left)):
        s = "%-{wl}s*%{wr}s".format(wl = max_left, wr = max_right)
        out.append(s % (left[i], right[i]))
    return out
