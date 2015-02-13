from test.assert_json      import assert_json
from topcoder.knights_tour import solution

def test_knights_tour ():
    assert_json('knights_tour', solution)
