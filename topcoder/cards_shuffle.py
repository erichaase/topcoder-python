"""
`CardsShuffle <http://community.topcoder.com/stat?c=problem_statement&pm=8295>`__
"""

def solution (cards, first, last, times):
    for _ in range(times):
        cards = cards[first - 1:last] + cards[:first - 1] + cards[last:]
    return cards
