"""
`ClientsList <http://community.topcoder.com/stat?c=problem_statement&pm=3520>`__
"""

import re

def solution (names):
    out = []
    for name in names:
        # match "First Last" format
        match = re.search(r'^\s*(\w+)\s+(\w+)', name)
        if match:
            out.append("%s %s" % (match.group(1), match.group(2)))
            continue

        # match "Last, First" format
        match = re.search(r'^\s*(\w+)\s*,\s*(\w+)', name)
        if match:
            out.append("%s %s" % (match.group(2), match.group(1)))
            continue

    out = sorted(out, key = lambda n: n.split()[0])
    out = sorted(out, key = lambda n: n.split()[1])
    return out
