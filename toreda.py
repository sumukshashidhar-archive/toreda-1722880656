"""
This is the file that, for all intents and purposed, we will run
"""


## intraday price testing


from src.bot.intraday import get_action as action
from src.datastream import datareader as datareader
from src.analysis.prophet_analysis import get_pred as prophet_analysis
import webbrowser
import os
import time

ticker = 'INFY.BSE'
interval = '1min'
keydb = datareader.read_keys()

# while True:
#     key, keydb = datareader.select_one_key(keydb)
#     df = datareader.intraday(ticker, interval, key)
#     t = action(df, ticker, to_open=False)
#     print(t[0])
#     webbrowser.open('file://'+ os.path.realpath(t[1]), new=0)
#     time.sleep(10)


## fbprophet predictions

key, keydb = datareader.select_one_key(keydb)
df = datareader.interday(ticker, key)
prophet_analysis(df)