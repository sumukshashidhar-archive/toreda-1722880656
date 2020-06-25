import numpy as np
import pandas as pd

def WMA(data, n):

    ws = np.zeros(data.shape[0])
    t_sum = sum(range(1, n+1))
    for i in range(n-1, data.shape[0]):
        ws[i] = sum(data[i-n+1 : i+1] * np.linspace(1, n, n))/ t_sum
        
    return ws


def get_mavs(df, freq=[5, 10, 20], n=7):
    if len(df.index) < max(freq):
        return False
    for i in freq:
        df[f'WMA{i}'] = WMA(df['close'], i)
    df['EWMA'] = df['close'].ewm(ignore_na=False, min_periods=n - 1, span=n).mean()
    df['EWMA_MEAN'] = df['EWMA'].ewm(ignore_na=False, min_periods=n- 1,span=n).mean()
    df['DEWMA'] = 2 * df['EWMA'] - df['EWMA_MEAN']
    nx = n*2
    df['Momentum'] = df['close'] - df['close'].shift(nx)
    df = df.iloc[max(freq):]
    return df
