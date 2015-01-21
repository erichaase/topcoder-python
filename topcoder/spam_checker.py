"""
`SpamChecker <http://community.topcoder.com/stat?c=problem_statement&pm=13119>`__
"""

def solution (log, good, bad):
    score = 0
    # iterate through lines and calculate score
    for line in log:
        if line == 'o':
            score += good
        elif line == 'x':
            score -= bad
        if score < 0:
            return "SPAM"
    return "NOT SPAM"
