import unittest
import analysis.datareader as datareader


class Test(unittest.TestCase):
    def test_read_keys(self):
        x = datareader.read_keys()
        self.assertEqual(type(x), type([]), "Did not return a list")
        self.assertNotEqual(len(x), 0, "list does not have anything")

    def test_create_keylogs(self):
        x = datareader.create_keylogs(datareader.read_keys())
        self.assertEqual(type(x), type({}), "Did not return a dictionary")
        self.assertNotEqual(len(x.keys), 0, "dictionary does not have anything")
