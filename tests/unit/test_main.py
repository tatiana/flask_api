import unittest

from venus.main import main


class MainTestCase(unittest.TestCase):

    def test_main(self):
        response = main()
        expected = "Venus is running"
        self.assertEqual(response, expected)
