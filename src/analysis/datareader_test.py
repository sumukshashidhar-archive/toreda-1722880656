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
        df = datareader.intraday(ticker='AAPL', interval='1min', key=key)
        print(df)
        self.assertEqual(type(df), type(pd.DataFrame()), "did not get a dataframe")

    def test_interday(self):
        keydb = datareader.read_keys()
        key, keydb = datareader.select_one_key(keydb)
        df = datareader.interday(ticker='AAPL', key=key)
        self.assertEqual(type(df), type(pd.DataFrame()), "did not get a dataframe")
