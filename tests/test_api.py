import pytest
from app import app
import tempfile

from tests.test_base import get_tests, recreate_database
from db.repository import get_currency_value


@pytest.fixture()
def client():
    app.config['TESTING'] = True
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    with app.test_client() as client:
        yield client


class TestCurrencies:

    @staticmethod
    def teardown_class():
        recreate_database()

    @staticmethod
    def setup():
        recreate_database()

    def test_get_positive(self, client):
        for url in get_tests('api', 'get_positive_case'):
            response = client.get(url)
            assert response.status_code == 200 and 'value' in response.get_json()

    def test_get_negative(self, client):
        for url in get_tests('api', 'get_negative_case'):
            response = client.get(url)
            assert response.status_code == 404

    def test_post_positive(self, client):
        for test in get_tests('api', 'post_positive_case'):
            response = client.post(test['url'], json=test['headers'])
            json_response = response.get_json()
            assert response.status_code == 200 and 'value' in json_response and \
                   json_response['value'] == test['value']

    def test_post_negative(self, client):
        for test in get_tests('api', 'post_negative_case'):
            response = client.post(test['url'], json=test['headers'])
            assert response.status_code == test['status']

    def test_put_positive(self, client):
        for test in get_tests('api', 'put_positive_case'):
            response = client.put(test['url'], json=test['headers'])
            check_value = get_currency_value(test['headers']['currency'])
            assert response.status_code == 200 and check_value == test['value']

    def test_put_negative(self, client):
        for test in get_tests('api', 'put_negative_case'):
            response = client.put(test['url'], json=test['headers'])
            assert response.status_code == test['status']


if __name__ == '__main__':
    pass
