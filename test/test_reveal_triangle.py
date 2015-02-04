from test.assert_json         import assert_json
from topcoder.reveal_triangle import solution

def test_reveal_triangle ():
    assert_json('reveal_triangle', solution)
