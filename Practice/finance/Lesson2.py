# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 13:14:50 2021
  Series
  Access 
  Calculation
  
@author: Ashok Kumar Jha
"""

import pandas as pd


# REading the CSV, Setting Index to First column of CSV, Changeing Data 
# type of Index to DateTime 
data = pd.read_csv("data/AAPL.csv",index_col=0,parse_dates=True)


print(type(data))

print(data)

print(data['Close'])
daily_change= data['Open'] - data['Close']
daily_pchange= (data['Open'] - data['Close'])*100/data['Open']

print(type(daily_change))
print(daily_change)
print(type(daily_pchange))
print(daily_pchange)

# each day Normalize like gaining in closing price from begining price 
norm = data['Close']/data['Close'].iloc[0]
print(norm)

# 5th day closing price
print(data['Close'].iloc[6])
print(data['Close'].iloc[0]*norm[6])
# Last day closing price
print(data['Close'].iloc[-1])
print(data['Close'].iloc[0]*norm[-1])
