# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 16:37:36 2021

@author: Ashok Kumar Jha


"""

import numpy as np
import pandas_datareader as pdr
import datetime as dt
import pandas as pd
import fix_yahoo_finance as fyf

#Start Time


'''
How volatility represent the risk.
Calculation of Average True Range (ATR) – a volatility and risk measure.
How to visualize the volatility.
'''
start = dt.datetime(2020,1,1)


fyf.pdr_override()

# time series data of the historic stock prices of Netflix (ticker NFLX).
data = pdr.data.get_data_yahoo("NFLX", start) 

'''
Average True Range (ATR) is a technical analysis indicator,
' 'measures market volatility by decomposing the entire range of an asset price 
for that period 
Particular TrueRange TRi = max[H-L,|H-Cp|,|L-Cp|]
ATR =1/n * sum(TRi) for i=1 to n              
Where TRi = A particular True Range
      H = A particular High
      L= A particular low
      Cp = A previous close price
      n = A Time period employed
'''

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

# great way to get the maximum value of these is to create a DataFrame with 
# all the values

df=pd.concat([high_low,high_cp,low_cp],axis=1)

print('After concatenation')
print(df)
print(data)



#True Range
true_range = np.max(df,axis=1) 
print(true_range)

# get the ATR as the moving average of 14 days (14 days is the default).
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

'''
This shows how the ATR moves in relation to the stock price. The blue line is 
ATR and the orange (semitransparent is the stock price).

In periods with big changes in price, the ATR moves up. When the price is more
 staple, the ATR moves down.

'''

