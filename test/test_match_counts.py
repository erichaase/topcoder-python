from test.assert_json      import assert_json
from topcoder.match_counts import solution

def test_match_counts ():
    assert_json('match_counts', solution)
