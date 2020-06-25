import unittest
import analysis.datareader as datareader
import pandas as pd


class Test(unittest.TestCase):
    def test_read_keys(self):
        x = datareader.read_keys()
        self.assertEqual(type(x), type({}), "Did not return a dictionary")
        self.assertNotEqual(len(x.keys()), 0, "dic does not have anything")

    def test_select_one_key(self):
        a, _ = datareader.select_one_key(datareader.read_keys())
        self.assertEqual(type(a), type(''), f"Did not get back a string or a key, got back {a}")

    def test_intraday(self):
        keydb = datareader.read_keys()
        key, keydb = datareader.select_one_key(keydb)
        df = datareader.intraday(ticker='INFY.BSE', interval='1min', key=key)
        # print(df)
        self.assertEqual(type(df), type(pd.DataFrame()), "did not get a dataframe")

    def test_interday(self):
        keydb = datareader.read_keys()
        key, keydb = datareader.select_one_key(keydb)
        df = datareader.interday(ticker='INFY.BSE', key=key)
        self.assertEqual(type(df), type(pd.DataFrame()), "did not get a dataframe")


    def test_key_reset(self):
        ls = []
        keydb = datareader.read_keys()
        for i in range(3):
            key, keydb = datareader.select_one_key(keydb)
            if key in ls:
                self.assertEqual(False, True, "The key was used before")
            else:
                ls.append(key)
