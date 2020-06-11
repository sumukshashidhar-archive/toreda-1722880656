#this will stream data using alphavantage

import pandas as pd

SYMBOL = 'NSE:INFY'
INTERVAL = '5min'
API_KEY = input()
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={SYMBOL}&interval={INTERVAL}&apikey={API_KEY}&datatype=csv'


df = pd.read_csv(url)

print(df.head)
