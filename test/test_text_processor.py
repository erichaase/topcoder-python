from test.assert_json        import assert_json
from topcoder.text_processor import solution

def test_text_processor ():
    assert_json('text_processor', solution)
