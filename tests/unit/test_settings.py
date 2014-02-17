import unittest

from venus import settings


class SettingsTestCase(unittest.TestCase):

    def test_has_attributes(self):
        self.assertTrue(settings.LOG_FILE_PATH)

    def test_attributes_values(self):
        self.assertEqual(settings.LOG_FILE_PATH, "/tmp/venus.log")
