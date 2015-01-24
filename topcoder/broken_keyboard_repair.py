"""
`BrokenKeyboardRepair <http://community.topcoder.com/stat?c=problem_statement&pm=7555>`__
"""

def solution (word):
    # calculate counts for each key
    counts = {}
    for char in word:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return len(counts.keys())
