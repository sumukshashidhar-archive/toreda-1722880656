#this will stream data using alphavantage

import pandas as pd
import time
import os
import visualize





## blanking out the file before we start
def refreshData(SYM, INT, KEY):
	SYMBOL = SYM
	INTERVAL = INT
	API_KEY = KEY
	url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={SYMBOL}&interval={INTERVAL}&apikey={API_KEY}&datatype=csv'
	filepath = f'./logs/streamdata-{SYMBOL}-{INTERVAL}.csv'
	a = time.time()	
	df = pd.read_csv(url)
	print(df.head())
	df.to_csv(filepath)
	visualize.viz(df)
	b = time.time()

	r = b - a
	
	with open('./logs/timedata.csv', 'a') as f:
		f.write(f'{r}\n')

def buy_or_sell():


refreshData('INFY.BO', '1min', 'VJOJOA8WIN0QEPCF')