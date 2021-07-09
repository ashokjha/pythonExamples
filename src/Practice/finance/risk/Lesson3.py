# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 18:04:04 2021

@author: Ashok Kumar Jha
"""

'''
Sharp ratio: combine Risk and Return in one measure.
Covered:
    Risk and return combined in one number.
    Using standard deviation as a measure for risk.
    Sharpe Ratio calculation combining risk and return.
    
The idea with Sharpe Ratio, is to have one number to represent both
 return and risk. This makes it easy to compare different weights of
 portfolios.
 Formula:
     Sharp Ratio (SR) 
     = [Return of portfolio-Risk Free return]/Stnd Deviation of portfolio
Goal higher SR

1. The return of the portfolio we covered in lesson 1, 
but we will calculate it with log returns here.
2. It is custom for the risk free return to use the 10 Year Treasury Note, 
but as it has been low for long time, often 0 is used.
3. The standard deviation is a measure of the volatility, 
and is used here to represent the risk.This is similar to Average True Range.

To get started, we need to read time series data of historic stock prices for a portfolio. This can be done as follows.
'''

import numpy as np
import pandas_datareader as pdr
import datetime as dt


tickers = ['AAPL', 'MSFT','TWTR','IBM']
start = dt.datetime(2020, 1, 1)

'''
Where our portfolio will consist of the tickers for 
Apple, Microsoft, Twitter and IBM (AAPL, MSFT, TWTR, IBM).
 We read the data from start 2020 from the Yahoo! 
 Finance API using Pandas Datareader.

Finally, we only keep the Adjusted Close price.

'''
data = pdr.data.get_data_yahoo(tickers, start)
data = data['Adj Close']
print(data)
'''
Let’s assume our portfolio is balanced as follows, 
25%, 15%, 40%, and 20% to AAPL, MSFT, TWTR, IBM, respectively.
Then we can calculate the daily log return of the portfolio as follows.
'''
portfolio = [.25, .15, .40, .20]
log_return = np.sum(np.log(data/data.shift())*portfolio, axis=1)

'''
Where we use the np.log to take the logarithm of the daily change, 
we apply the portfolio. Finally, we sum (np.sum) along the rows (axis=1).


For the fun, we can visualize the daily log returns as follows.
'''

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
log_return.hist(bins=50, ax=ax)
'''
This gives an impression of how volatile the portfolio is. 
The more data is centered around 0.0, the less volatile and risky.

The Sharpe Ratio can be calculate directly as follows.
'''
sharpe_ratio = log_return.mean()/log_return.std()

'''
This gives a daily Sharpe Ratio, where we have the return to be the mean value.
That is, the average return of the investment. And divided by the 
standard deviation.

The greater is the standard deviation the greater the magnitude of the 
deviation from the mean value can be expected.

To get an annualized Sharpe Ratio.
'''
asr = sharpe_ratio*252**.5
print("ASR =",asr)




'''
 In the next lesson about Monte Carlo Simulations for Portfolio Optimization.
 '''