from test.assert_json            import assert_json
from topcoder.tournament_judging import solution

def test_tournament_judging ():
    assert_json('tournament_judging', solution)
