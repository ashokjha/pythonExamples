# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 16:57:48 2021

@author: Ashok Kumar Jha
"""
import numpy as np
import pandas_datareader.data as pdr
import datetime as dt
import pandas as pd
import fix_yahoo_finance as fyf

#Start Time
start = dt.datetime(2015,1,1)
fyf.pdr_override()

data = pdr.get_data_yahoo("NFLX", start) 
print(data.head())




# High - Low
print('High - Low')
high_low=data['High']-data['Low']
print(high_low)

# High - Previous Close
print('High - Previous Close')
high_cp =np.abs(data['High']-data['Close'].shift())
print(high_cp)

# Low - Previous Close
print('Low - Previous Close')
low_cp =np.abs(data['Low']-data['Close'].shift())
print(low_cp)

# Concatenate in data alomng column

df=pd.concat([high_low,high_cp,low_cp],axis=1)
print('After concatenation')
print(df)
print(data)

#True Range
true_range = np.max(df,axis=1) 
print(true_range)

# Average True range
average_true_range = true_range.rolling(14).mean()
print(average_true_range)

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

average_true_range.plot(ax=ax)
ax2=data['Close'].plot(ax=ax,secondary_y=True, alpha=.3)
ax.set_xlabel('Date')
ax.set_ylabel('ATR')
ax2.set_ylabel('Price')
ax.set_title('NFLX volatility')

