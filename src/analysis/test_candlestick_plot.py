import unittest
import analysis.datareader as datareader
import pandas as pd

#files
import analysis.candlestick_plot as candlestick_plot


class Test(unittest.TestCase):
    def test_plot_intraday(self):
        keydb = datareader.read_keys()
        key, keydb = datareader.select_one_key(keydb)
        df = datareader.intraday('INFY.BSE', '1min', key)
        t = candlestick_plot.plot_intraday(df, 'INFY.BSE', False)
        self.assertEqual(len(t), 2, "Wrong length tuple")
        self.assertEqual(t[0], True, "Did not get True")
        self.assertEqual(type(t[1]), type(''), "Did not get filepath")