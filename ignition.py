import numpy as np
import pandas as pd
import nsepy
import datetime as dt
import functions_part1 as fp1
import functions_part2 as fp2
from bokeh import plotting as plt

# Importing the dataset
infy_data = nsepy.get_history(symbol='INFY',start=dt.date(2015,1,1),
                              end=dt.date(2015,12,31))

tcs_data = nsepy.get_history(symbol='TCS',start=dt.date(2015,1,1),
                              end=dt.date(2015,12,31))

nifty_it_data = nsepy.get_history(symbol='NIFTYIT',index=True,start=dt.date(2015,1,1),
                              end=dt.date(2015,12,31))


#Q1.1
# These are the dataframes that hold values for n-week moving averages
infy_close_mov = pd.DataFrame(columns=['4','16','28','40','52'])
tcs_close_mov = pd.DataFrame(columns=['4','16','28','40','52'])
nifty_it_close_mov = pd.DataFrame(columns=['4','16','28','40','52'])
    
for i in range(4,53,12):
    infy_close_mov[str(i)] = fp1.get_moving_avg(infy_data,'Close',i)
    tcs_close_mov[str(i)] = fp1.get_moving_avg(tcs_data,'Close',i)
    nifty_it_close_mov[str(i)] = fp1.get_moving_avg(nifty_it_data,'Close',i)

#Q1.2
infy_mov = fp1.get_moving_avg(infy_data,None,10)
tcs_mov = fp1.get_moving_avg(tcs_data,None,10)
nifty_it_mov = fp1.get_moving_avg(nifty_it_data,None,10)
    
infy_75_mov = fp1.get_moving_avg(infy_data,None,75)
tcs_75_mov = fp1.get_moving_avg(tcs_data,None,75)
nifty_it_75_mov = fp1.get_moving_avg(nifty_it_data,None,75)

#Q1.3
infy_vol_shock = fp1.get_series(data=infy_data,col='Volume',threshold=0.1,dirn=False)
infy_vol_dir_shock = fp1.get_series(data=infy_data,col='Volume',threshold=0.1,dirn=True)

tcs_close_shock = fp1.get_series(data=tcs_data,col='Close',threshold=0.02,dirn=False)
tcs_close_dir_shock = fp1.get_series(data=tcs_data,col='Close',threshold=0.02,dirn=True)


#Q2
plt.show(fp2.plot_series(infy_data,'Close'))
