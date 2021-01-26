import json
from db.repository import init_database, drop_database


def get_tests(tests_group, tests_name: str):
    with open(f'test_cases/{tests_group}/{tests_name}.json') as test_file:
        for test in json.load(test_file):
            yield test


def recreate_database():
    drop_database()
    init_database()
