"""
This is to calculate the percentage change between two intervals of a graph
"""

import analysis.datareader as datareader
import numpy as np


def get_pct_change(seq_close):
    pct_c = seq_close.pct_change()
    daily_pct_c = seq_close.pct_change()
    daily_pct_c.fillna(0, inplace=True)
    daily_log_returns = np.log(seq_close.pct_change()+1)
    returns = seq_close / seq_close.shift(1) - 1

    
