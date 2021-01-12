import unittest
from app import app


class Base(unittest.TestCase):
    def set_up(self):
        self.app = app.test_client()

    def get_test(self):
        response = self.app.get('/get_currencies/USD')
        self.assertEqual(response.status_code, 200)
        response = self.app.get('/get_currencies')
        self.assertEqual(response.status_code, 404)
        response = self.app.get('/get_currencies/UUs3')
        self.assertEqual(response.status_code, 404)

    def post_test(self):
        headers = {
            "from": "USD",
            "to": "RUB",
            "value": 1
        }
        response = self.app.post('/get_currencies', headers=headers)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
