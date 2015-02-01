from test.assert_json        import assert_json
from topcoder.grocery_bagger import solution

def test_grocery_bagger ():
    assert_json('grocery_bagger', solution)
