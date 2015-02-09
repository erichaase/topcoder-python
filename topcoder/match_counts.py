"""
`MatchCounts <http://community.topcoder.com/stat?c=problem_statement&pm=4798>`__
"""

def solution (people):
    return len(solve(0, people, "NNNNNN"))

def solve (i, people, tasks):
    if i >= len(people):
        return [tasks]

    l = []
    for ability in people[i]:
        ability = int(ability)
        if tasks[ability] == "N":
            tasks_assigned = tasks[:ability] + str(i) + tasks[ability + 1:]
            l += solve(i + 1, people, tasks_assigned)
    return l

"""
01 23 NNNNNN
    23 0NNNNN
        0N1NNN
        0NN1NN
    23 N0NNNN
        N01NNN
        N0N1NN
"""
