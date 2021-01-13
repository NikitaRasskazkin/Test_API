import unittest
from app import app
from db.models import Currencies


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_positive(self):
        response = self.app.get('/get_currencies/USD')
        self.assertEqual(response.status_code, 200)

    def test_get_negative(self):
        url_list = [
            '/get_currencies',
            '/get_currencies/US',
            '/',
            '/bad_url'
        ]
        with self.app:
            for url in url_list:
                response = self.app.get(url)
                self.assertEqual(response.status_code, 404)

    def test_post_positive(self):
        headers = {
            "from": "USD",
            "to": "RUB",
            "value": 1
        }
        response = self.app.post('/get_currencies', json=headers)
        self.assertEqual(response.status_code, 200)

    def test_post_negative(self):
        headers = {
            "from": "US",
            "to": "RUB",
            "value": 1
        }
        response = self.app.post('/get_currencies', json=headers)
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
