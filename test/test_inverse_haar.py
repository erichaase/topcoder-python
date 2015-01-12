from test.assert_json      import assert_json
from topcoder.inverse_haar import solution

def test_inverse_haar ():
    assert_json('inverse_haar', solution)
