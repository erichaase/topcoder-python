from test.assert_json      import assert_json
from topcoder.clients_list import solution

def test_clients_list ():
    assert_json('clients_list', solution)
