"""
`KnightsTour <http://community.topcoder.com/stat?c=problem_statement&pm=10577>`__
"""

def solution (board):
    b, n = Board(board), 1
    while b.update(): n += 1
    return n

class Board:
    def __init__ (self, board):
        self.board = [list(row) for row in board]

    def update (self):
        k, t = self.next_move()
        if k and t:
            self.board[k[0]][k[1]] = "*"
            self.board[t[0]][t[1]] = "K"
            return True
        else:
            return False

    def next_move (self):
        k = self.knight()

        m = self.moves(k)
        m.sort(key = lambda p: p[1])
        m.sort(key = lambda p: p[0])
        m.sort(key = lambda p: len(self.moves(p)))

        t = None
        if len(m) > 0:
            t = m[0]

        return k, t

    def knight (self):
        for x, row in enumerate(self.board):
            for y, cell in enumerate(row):
                if cell == "K":
                    return x, y
        return None, None

    def moves (self, p):
        x, y = p[0], p[1]
        targets = [
            [x - 2, y - 1],
            [x - 2, y + 1],
            [x - 1, y + 2],
            [x + 1, y + 2],
            [x + 2, y - 1],
            [x + 2, y + 1],
            [x - 1, y - 2],
            [x + 1, y - 2],
        ]

        m = []
        for target in targets:
            if self.valid(target):
                m.append(target)
        return m

    def valid (self, p):
        x, y = p[0], p[1]
        if x < 0:
            return False
        if x >= len(self.board):
            return False
        if y < 0:
            return False
        if y >= len(self.board[0]):
            return False

        c = self.board[x][y]
        if c == "*":
            return False
        if c == "K":
            return False
        if c == ".":
            return True
        return False

    def __str__ (self):
        s = ""
        for row in self.board:
            s += "".join(row)
            s += "\n"
        return s
