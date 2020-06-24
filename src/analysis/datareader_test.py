import unittest

from datareader import testingtest

class Test(unittest.TestCase):

    def test_testingtest(self):
        # testing the test module

        self.assertEqual(testingtest(), True)
        self.assertEqual(testingtest(), False)



