from datetime import date
from datetime import timedelta
from alpha_vantage.timeseries import TimeSeries 
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import time
import os
import webbrowser


SYMBOL = input("Enter the Symbol you want to check for")
INTERVAL = '1min'
API_KEY = 'VJOJOA8WIN0QEPCF'


def pullnplot():
    ts = TimeSeries(key=API_KEY, output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=SYMBOL, interval=INTERVAL, outputsize='compact')
    df = data[:]
    df = df.sort_values(by='date')
    df = df.reset_index()
    print(df.tail())
    df = df.iloc[df[df['date'] == str(str(date.today() - timedelta(days=1)) +  ' 23:45:00')].index.values[0]:]
    
    print(df.tail())

    fig1 = go.Figure(data=[go.Candlestick(x=df['date'],
                    open=df['1. open'],
                    high=df['2. high'],
                    low=df['3. low'],
                    close=df['4. close'])])
    fig1.update_layout(template='plotly_white', xaxis_range=[str(str(date.today() - timedelta(days=1)) +  ' 23:44:00'), str(str(date.today()) + ' 06:00:00')])

    filename = f'./{SYMBOL}-{date.today()}.html'
    fig1.write_html(filename)
    return filename


while True:
    filename = pullnplot()
    webbrowser.open('file://' + os.path.realpath(filename), new=0) 
    print("Refreshed")
    time.sleep(30)
