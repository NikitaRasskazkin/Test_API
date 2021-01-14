import pytest
from app import app
import json
import tempfile
import os


def open_tests(test_name: str):
    with open(f'test_cases/{test_name}.json') as test_file:
        return json.load(test_file)


@pytest.fixture()
def client():
    app.config['TESTING'] = True
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    with app.test_client() as client:
        yield client
    os.close(db_fd)


def test_get_positive(client):
    usl_list = open_tests('get_positive_case')
    for url in usl_list:
        response = client.get(url)
        assert response.status_code == 200 and 'value' in response.get_json()


def test_get_negative(client):
    url_list = open_tests('get_negative_case')
    for url in url_list:
        response = client.get(url)
        assert response.status_code == 404


def test_post_positive(client):
    tests = open_tests('post_positive_case')
    for test in tests:
        response = client.post(test['url'], json=test['headers'])
        assert response.status_code == 200 and 'value' in response.get_json()


def test_post_negative(client):
    tests = open_tests('post_negative_case')
    for test in tests:
        response = client.post(test['url'], json=test['headers'])
        assert response.status_code == 404


if __name__ == '__main__':
    pass
