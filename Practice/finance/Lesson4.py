# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 19:52:05 2021
MACD, MACD, short for moving average convergence/divergence, is a trading
    indicator used in technical analysis of stock prices.
The MACD indicator(or "oscillator") is a collection of three time series
calculated from historical price data, most often the closing price. These
three series are: the MACD series proper, the "signal" or "average" series,
and the "divergence" series which is the difference between the two

Calculation
    MACD=12-Period EMA-26-Period EMA
    Singal line 9 - period EMA of MACD


Sochastic oscillator:A stochastic oscillator is a momentum indicator comparing
a particular closing price of a security to a range of its prices over a
certain period of time. The sensitivity of the oscillator to market movements
is reducible by adjusting that time period or by taking a moving average of the
result.It is used to generate overbought and oversold trading signals,
utilizing a 0–100 bounded range of values.

Calculation
14-high: Maximum of last 14 trading days
14-low: Minimum of last 14 trading days
%K: (last close-14-low)*100/(14-high-14-low))
%D: Simple Moving Average of %K (preferable 3 days)

@author: Ashok Kumar Jha
"""

import pandas as pd

from matplotlib import pyplot as plt

data = pd.read_csv("data/AAPL.csv", index_col=0, parse_dates=True)
print(data.head())

# MACD
exp1 = data['Close'].ewm(span=12, adjust=False).mean()
exp2 = data['Close'].ewm(span=26, adjust=False).mean()
data['MACD'] = exp1-exp2
data['Signal Line'] = data['MACD'].ewm(span=9, adjust=False).mean()
print(data.head())
fig, ax = plt.subplots()

data[['MACD', 'Signal Line']].plot(ax=ax)
data['Close'].plot(ax=ax, alpha=0.25, secondary_y=True, color='r')

# Sochastic oscillator
high14 = data['High'].rolling(14).max()
low14 = data['Low'].rolling(14).min()
data['%K'] = (data['Close']-low14)*100/(high14-low14)
data['%D'] = data['%K'].rolling(3).mean()
print(data.tail())

fig1, ax1 = plt.subplots()

data[['%K', '%D']].iloc[3*len(data)//4:].plot(ax=ax1)
ax1.axhline(80, c='r', alpha=0.3)
ax1.axhline(20, c='r', alpha=0.3)
data[['Close']].iloc[3*len(data)//4:].plot(
        ax=ax1, alpha=0.3, secondary_y=True)
