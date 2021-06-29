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

from TechAnalysis import TechAnalysis

ta = TechAnalysis()

# MACD
ta.macdGraph()

# Sochastic oscillator
ta.sochasticoscGraph()
print(ta.data.head())
