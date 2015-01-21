from test.assert_json      import assert_json
from topcoder.spam_checker import solution

def test_spam_checker ():
    assert_json('spam_checker', solution)
