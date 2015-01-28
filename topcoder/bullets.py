"""
`Bullets <http://community.topcoder.com/stat?c=problem_statement&pm=665>`__
"""

def solution (guns, bullet):
    for i, gun in enumerate(guns):
        if match(gun, bullet):
            return i
    return -1

def match(gun, bullet):
    for _ in range(len(gun)):
        if gun == bullet:
            return True
        gun = gun[1:] + gun[0]
    return False
