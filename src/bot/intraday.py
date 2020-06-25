import sys
import os
sys.path.append("..")
import pandas as pd
from analysis.mav import get_mavs as mav
from datastream import datareader  as datareader
from toreda_plot import toreda_plot as tp


keydb = datareader.read_keys()
key, keydb = datareader.select_one_key(keydb)

df = datareader.intraday('INFY.BSE', '1min', key)
df = mav(df)
print(df.head())

