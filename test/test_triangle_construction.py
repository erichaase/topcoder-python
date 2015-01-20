from test.assert_json               import assert_json
from topcoder.triangle_construction import solution

def test_triangle_construction ():
    assert_json('triangle_construction', solution)
