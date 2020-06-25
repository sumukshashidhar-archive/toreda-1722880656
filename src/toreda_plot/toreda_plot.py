import plotly.express as px
from datetime import date
import webbrowser
import os
from datetime import timedelta
import plotly.graph_objects as go
import time

def open_webbrowser(to_open, filename):
    if to_open:
        webbrowser.open('file://' + os.path.realpath(filename), new=0)


def get_histogram(data, freq, ticker, to_open=False):
    FILEPATH = f'./../Generated_Graphs/pct_changes/{freq}/{ticker}-{date.today()}.html'
    fig = px.histogram(x=data)
    fig.write_html(FILEPATH)
    open_webbrowser(to_open, FILEPATH)
    return True, FILEPATH

def plot_intraday(df, ticker, to_open=False):
    PLOT_FILEPATH = f'./../Generated_Graphs/candlesticks/interday/{ticker}-{date.today()}.html'
    fig1 = go.Figure(data=[go.Candlestick(x=df['timestamp'],
                                          open=df['open'],
                                          high=df['high'],
                                          low=df['low'],
                                          close=df['close'])])
    fig1.update_layout(template='plotly_dark', xaxis_range=[str(str(date.today() - timedelta(days=1)) + ' 23:44:00'),
                                                            str(str(date.today()) + ' 06:00:00')])

    fig1.write_html(PLOT_FILEPATH)
    open_webbrowser(to_open, PLOT_FILEPATH)
    return True, PLOT_FILEPATH


def mav(df, ticker, freq='intra', intervals=[5, 10, 20], to_open=False):
    PLOT_FILEPATH = f'./../Generated_Graphs/mavs/{freq}/{len(intervals)}-{ticker}-{date.today()}-{time.time()}.html'
    fig = px.line(template='plotly_dark')
    for i in intervals:
        fig.add_scatter(y = df[f'WMA{i}'], mode='lines', name=f'WMA - {i} {freq}')
    fig.add_scatter(y = df['EWMA'], mode='lines', name='EWMA')
    fig.add_scatter(y = df['DEWMA'], mode='lines', name='DEWMA')
    fig.add_scatter(y = df['close'], mode='lines', name='Actual Closing Prices')
    fig.write_html(PLOT_FILEPATH)
    open_webbrowser(to_open, PLOT_FILEPATH)
    return True, PLOT_FILEPATH
