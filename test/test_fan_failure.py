from test.assert_json     import assert_json
from topcoder.fan_failure import solution

def test_fan_failure ():
    assert_json('fan_failure', solution)
