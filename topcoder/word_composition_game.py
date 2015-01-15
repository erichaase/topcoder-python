"""
`WordCompositionGame <http://community.topcoder.com/stat?c=problem_statement&pm=4483>`__
"""

def solution (words_A, words_B, words_C):
    # create dictionary of counts
    count = {}
    for word in words_A + words_B + words_C:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    # format output with scores
    return "%d/%d/%d" % (
        score(count, words_A),
        score(count, words_B),
        score(count, words_C)
    )

# calculate score for player
def score (count, words):
    total = 0
    for word in words:
        n = count[word]
        if   n == 3:
            total += 1
        elif n == 2:
            total += 2
        elif n == 1:
            total += 3
    return total
