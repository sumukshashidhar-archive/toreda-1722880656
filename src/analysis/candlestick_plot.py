"""
Saves a candlestick plot of the requested data and opens if needed
"""

## modules
from datetime import date
from datetime import timedelta
import plotly.graph_objects as go
import os
import webbrowser


PLOT_FILEPATH = './../Generated_Graphs/candlesticks/interday/'


def plot_intraday(df, ticker, open):
    fig1 = go.Figure(data=[go.Candlestick(x=df['timestamp'],
                                          open=df['open'],
                                          high=df['high'],
                                          low=df['low'],
                                          close=df['close'])])
    fig1.update_layout(template='plotly_dark', xaxis_range=[str(str(date.today() - timedelta(days=1)) + ' 23:44:00'),
                                                            str(str(date.today()) + ' 06:00:00')])

    filename = f'{PLOT_FILEPATH}{ticker}-{date.today()}.html'
    fig1.write_html(filename)
    if open:
        webbrowser.open('file://' + os.path.realpath(filename), new=0)
    return True, filename

