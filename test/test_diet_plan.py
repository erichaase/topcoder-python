from test.assert_json   import assert_json
from topcoder.diet_plan import solution

def test_diet_plan ():
    assert_json('diet_plan', solution)
