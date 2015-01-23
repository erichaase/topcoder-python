"""
`DancingSentence <http://community.topcoder.com/stat?c=problem_statement&pm=5950>`__
"""

def solution (sentence):
    out       = ""
    nextUpper = True
    for char in sentence:
        if char == " ":
            out += char
            continue
        if nextUpper:
            out += char.upper()
        else:
            out += char.lower()
        nextUpper = not nextUpper
    return out
