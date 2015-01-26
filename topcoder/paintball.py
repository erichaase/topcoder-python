"""
`Paintball <http://community.topcoder.com/stat?c=problem_statement&pm=8060>`__
"""

def solution (players_lines, messages):
    # players and teams dicts indexed by name
    players = {}
    teams   = {}

    # parse first argument: lines of players
    for player_line in players_lines:
        name, team = player_line.split()
        player     = Player(name, team)

        players[name] = player
        if not team in teams:
            teams[team] = Team(team)
        teams[team].players.append(player)

    # parse second argument: list of actions
    for message in messages:
        name_shooter, _, name_shot = message.split()
        shooter = players[name_shooter]
        shot    = players[name_shot]

        if shooter.team == shot.team:
            shooter.score -= 1
        else:
            shooter.score += 1
            shot.score    -= 1

    # format list of strings output
    out = []
    t1 = reversed(sorted(teams.values(), key=lambda team: team.name))
    t2 = reversed(sorted(t1            , key=lambda team: team.score()))
    for team in t2:
        out.append(str(team))
        p1 = reversed(sorted(team.players, key=lambda player: player.name))
        p2 = reversed(sorted(p1,           key=lambda player: player.score))
        for player in p2:
            out.append(str(player))
    return out

class Player:
    def __init__ (self, name, team):
        self.name  = name
        self.team  = team
        self.score = 0
    def __str__ (self):
        return " %s %d" % (self.name, self.score)

class Team:
    def __init__ (self, name):
        self.name    = name
        self.players = []
    def score (self):
        return sum([player.score for player in self.players])
        #return reduce(lambda x, y: x + y, [player.score for player in self.players])
    def __str__ (self):
        return "%s %d" % (self.name, self.score())
