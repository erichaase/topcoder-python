from test.assert_json               import assert_json
from topcoder.word_composition_game import solution

def test_word_composition_game ():
    assert_json('word_composition_game', solution)
