import json

def assert_json (name, solution):
    for testcase in json.load(open('test/test_%s.json' % name)):
        args      = testcase[:-1]
        expected  = testcase[-1]
        result    = solution(*args)
        assert result == expected
