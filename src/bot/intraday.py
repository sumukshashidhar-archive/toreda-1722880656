import sys
import os

sys.path.append(os.path.realpath('.'))
sys.path.append(os.path.realpath('./../'))
import pandas as pd
from src.analysis.mav import get_mavs as mav
from src.datastream import datareader  as datareader
from src.toreda_plot import toreda_plot as tp


def get_action(df, ticker, to_open=False, safety_threshold=5):
    df = mav(df)
    _, file = tp.mav_simple(df, ticker, to_open=to_open)
    analyze = df[-5:].copy()
    analyze.reset_index(inplace=True)
    score = 100
    for i in analyze.index:
        if analyze['WMA5'][i] > analyze['WMA20'][i]:
            score += 10
        else:
            score -= 10
    if score > 90:
        return "SELL", file
    return "BUY", file
