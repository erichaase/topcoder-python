"""
`TextProcessor <http://community.topcoder.com/stat?c=problem_statement&pm=6002>`__

Old procedural solution:
    chars = []
    for char in text:
        if re.match(r'[A-Za-z]', char):
            chars.append(char.lower())
    return "".join(sorted(chars))

Alternative functional solution:
    l = filter(lambda x: False if re.match(r'\s|\d', x) else True, list(text))
    l = map(lambda x: x.lower(), l)
    return "".join(sorted(l))
"""

import re

def solution (text):
    return "".join(sorted(map(convert, list(text))))

def convert (char):
    if re.match(r'\s|\d', char):
        return ""
    else:
        return char.lower()
