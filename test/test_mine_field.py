from test.assert_json    import assert_json
from topcoder.mine_field import solution

def test_mine_field ():
    assert_json('mine_field', solution)
