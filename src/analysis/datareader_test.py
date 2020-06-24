import unittest

import datareader

class Test(unittest.TestCase):

    def test_read_keys(self):
        x = datareader.read_keys()
        self.assertEqual(type(x), type([]), "Did not return a list")
        self.assertNotEqual(len(x), 0, "list does not have anything")


