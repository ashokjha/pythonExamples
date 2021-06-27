# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 13:51:19 2021
Technical Analysis
Calculate with Column
 Add Column
 Drop Column
 Min, Max,ArgMin,ArgMax
 Mean
@author: Ashok Kumar Jha
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


# REading the CSV, Setting Index to First column of CSV, Changeing Data
# type of Index to DateTime
data = pd.read_csv("data/AAPL.csv", index_col=0, parse_dates=True)

# Adding Data Column
data["daily_ch"] = data['Open'] - data['Close']

data["normalize"] = data['Close']/data['Close'].iloc[0]
data["%-Change"] = data['Close'].pct_change()

data["Log Returns"] = np.log(data['Close']/data['Close'].shift())

print(data.head())

print('Over all Minimum value in every Column')
print(data.min())

print('Minimum value in every Column and index')
print('daily_ch minimum :', data['daily_ch'].min(),
      ' and index:', data['daily_ch'].idxmin())

print('Over all Maximum value in every Column')
print(data.max())
print('Close Maximum :', data['Close'].max(), ' and index:',
      data['Close'].idxmax())
print('Close Maximum :', data['Close'].max(), ' and index:',
      data['Close'].idxmax())

stddev = data["Log Returns"].std()

volatility = stddev*(252**.5)
print("Standrad Deviation: {0}  Volaitility: {1}".format(stddev, volatility))

vltstr = str(round(volatility, 4)*100)

fig, ax = plt.subplots()

data["Log Returns"].plot.hist(ax=ax, bins=50, alpha=0.6, color='b')
ax.set_xlabel('Log Return')
ax.set_ylabel('Freq of Log return')
ax.set_title('AAPL volatility: '+vltstr)

# Moving Average 10 day
data['MVA 10'] = data['Close'].rolling(10).mean()

# Exponential Moving Average 10 day
data['EMA 10'] = data['Close'].ewm(span=10, adjust=False).mean()

fig, ax = plt.subplots()
# data[['MVA 10','EMA 10']].plot(ax=ax)
print('Lesser Data')
data[['MVA 10', 'EMA 10']].loc['2020-12-01':].plot(ax=ax)
ax.set_title("Actual, Moving Average and Exponential Moving Average")
data[['Close']].loc['2020-12-01':].plot(ax=ax,alpha=0.25)
