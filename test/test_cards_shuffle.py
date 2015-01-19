from test.assert_json       import assert_json
from topcoder.cards_shuffle import solution

def test_cards_shuffle ():
    assert_json('cards_shuffle', solution)
