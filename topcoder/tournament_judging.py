"""
`TournamentJudging <http://community.topcoder.com/stat?c=problem_statement&pm=9822>`__
"""

def solution (scores, conv):
    total = 0
    for i in range(len(scores)):
        total += round(float(scores[i]) / conv[i])
    return total
