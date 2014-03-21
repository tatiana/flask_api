import unittest

from venus.main import app


class MainTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_healthcheck(self):
        response = self.app.get('/healthcheck')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(), b'Atchim!')

    def test_number_one(self):
        response = self.app.get('/numbers/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(), b'one')

    def test_number_five(self):
        response = self.app.get('/numbers/5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(), b'five')
