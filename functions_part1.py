import numpy as np
import pandas as pd

def get_moving_avg(data, col, w):
    if col:
        return data[col].rolling(window=w).mean()
    else:
        return data.rolling(window=w).mean()

def get_series(data,col,threshold,dirn):
    series = pd.Series()
    if dirn:
        series = data[col].pct_change()>threshold        
        series = series*1
    else:
        series = np.abs(data[col].pct_change())>threshold
    return series
    