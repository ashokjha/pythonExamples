# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 16:57:48 2021

@author: Ashok Kumar Jha
"""
import numpy as np
import pandas_datareader.data as pdr
import datetime as dt


#Start Time
'''
historic time series stock prices of  Apple (ticker AAPL) starting from 2020 
and up until today.
'''
start = dt.datetime(2020,1,1)


# fyf.pdr_override()

data = pdr.get_data_yahoo("AAPL", start) 
print(data.head())

#The index is DatetimeIndex. 
#This makes it possible to take advantage of being a time series.
print(data.index)


# Convert DataFrame Type to Numpy Type

arrdata = data.to_numpy()

print(arrdata)

#Datatype of data
print(data.dtypes)

#Datatype of numpy
print(arrdata.dtype)

#Shape
print(data.shape, arrdata.shape)

# Tiop 10 data from numpy array
small = arrdata[:10, 0].copy()

print(small)

print(np.max(small))
print(small.max())
print(small.argmax())  # Index of maximum value

# We can apply logarithm on numpy as well data frame data

print(np.log(small))
print(np.log(data))

# Daily Return
print(data/data.shift())

print(np.sum(np.log(data/data.shift())))



# Getting data from multiple tickers
tickers = ['AAPL', 'MSFT', 'TWTR', 'IBM']
start = dt.datetime(2020, 1, 1)

data = pdr.get_data_yahoo(tickers, start)

print(data)

adata = data['Adj Close']
print(adata)

# Now consider a portfolio as follows.
# 5%, 15%, 40%, and 20% to AAPL, MSFT, TWTR, and IBM, respectively.
portfolios = [.25, .15, .40, .20]
# Assume we have 10000 USD to invest as above.
# First we normalize the data with data/data.iloc[0]
# multiply with the portfolio and the amount we invest.


print((adata/adata.iloc[0])*portfolios*100000)

#the sum of the full return as follows.

print(np.sum((adata/adata.iloc[0])*portfolios*100000,axis=1))
