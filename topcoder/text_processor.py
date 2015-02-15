"""
`TextProcessor <http://community.topcoder.com/stat?c=problem_statement&pm=6002>`__
"""

import re

def solution (text):
    chars = []
    for char in text:
        if re.match(r'[A-Za-z]', char):
            chars.append(char.lower())
    return "".join(sorted(chars))
