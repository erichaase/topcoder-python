"""
`ProseFlip <http://community.topcoder.com/stat?c=problem_statement&pm=4639>`__
"""

def solution (strings):
    l = [""] * len(strings[0])
    for string in strings:
        for i, char in enumerate(string):
            l[i] += char
    return l
