# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 20:01:30 2021

@author: Ashok Kumar Jha
"""

# Yahoo recently has become an unstable data source.
# If it gives an error, you may run the cell again, or try yfinance
#import pandas as pd

from pandas_datareader import data as pdr

import datetime as dt


start_date = dt.datetime(1990,1,1)
end_date = dt.datetime(2001,3,31)
# Set the ticker
ticker = 'AMZN'

print(type(pdr))
# Get the data
data = pdr.get_data_yahoo(ticker, start_date, end_date)
print(type(data.t))
print(data.head())




'''
import pandas_datareader as pdr
import datetime as dt
 
ticker = "AAPL"
start = dt.datetime(2019, 1, 1)
end = dt.datetime(2020, 12, 31)
 
data = pdr.get_data_yahoo(ticker, start, end)

print(data)
'''