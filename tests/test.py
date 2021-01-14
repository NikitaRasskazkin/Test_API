import pytest
from app import app
import json


def open_tests(test_name: str):
    with open(f'test_cases/{test_name}.json') as test_file:
        return json.load(test_file)


class Test:
    def setup(self):
        self.app = app.test_client()

    def test_get_positive(self):
        usl_list = open_tests('get_positive_case')
        for url in usl_list:
            response = self.app.get(url)
            assert response.status_code == 200 and 'value' in response.get_json()

    def test_get_negative(self):
        url_list = open_tests('get_negative_case')
        for url in url_list:
            response = self.app.get(url)
            assert response.status_code == 404

    def test_post_positive(self):
        tests = open_tests('post_positive_case')
        for test in tests:
            response = self.app.post(test['url'], json=test['headers'])
            assert response.status_code == 200 and 'value' in response.get_json()

    def test_post_negative(self):
        tests = open_tests('post_negative_case')
        for test in tests:
            response = self.app.post(test['url'], json=test['headers'])
            assert response.status_code == 404


if __name__ == '__main__':
    pass
