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
from matplotlib import pyplot as plt
from configparser import RawConfigParser
import src.Practice.finance.ReadYFinance as ryf


class TechAnalysis:
    DATA_FILE = "data/AAPL.csv"
    '''
        Financial Technical Analysis
    '''
    def __init__(self, cfg=None):
        '''
            Initialize with configuration
        '''
        self.config = cfg
        # Approx Number of Trading Day In Year
        self.NUMOFTD = 252
        print(self.config)

        if cfg is None:
            '''
                Example used csv file
            '''
            self.data = pd.read_csv(self.DATA_FILE, index_col=0,
                                    parse_dates=True)
        else:
            '''
            Load the data as per configuration
            '''
            self.data = ryf.getYFData(self.config)

    def addDailyChange(self, stcol='Open', clcol='Close'):
        '''
            Add Daily Change in dataframe
            stcol : Starting column default Open
            clcol : End Day Column default Close
            Requisite data is available
        '''
        self.data["daily_ch"] = self.data[stcol] - self.data[clcol]

    def addnormalize(self, col='Close'):
        '''
            Add Normalize Column in dataframe
            col:Data Column for which Normalize needed default Close
            Requisite data is available
        '''
        self.data["normalize"] = self.data[col]/(self.data[col].iloc[0])

    def addpchange(self, col='Close'):
        '''
            Add % change Column in dataframe
            col:Data Column for which % Change needed default Close
            Requisite data is available
        '''
        self.data["%-Change"] = self.data[col].pct_change()

    def addlogreturns(self, col='Close'):
        '''
            Add log returns Column  in dataframe
            Description : logarithmic return, continuously compounded return
            col:Data Column for which Log Return required default Close
            Requisite data is available
        '''
        self.data["Log Returns"] = self.data[col]/self.data[col].shift()

    def addMovingAverage(self, d=10, col='Close'):
        '''
            Add Moving Average Column in dataframe
            d: Number of days of Moving Average should be positive integer
            col: Data set column for moving average needed Default 'Close'
            Description : Moving Averge,series of averages of different subsets
            of the full data set. In Finance its Stock Indicator
            Requisite data is available
        '''
        if not isinstance(d, int) or d < 1:
            raise ValueError("Not a a positive Number")
        self.data["MVA"] = self.data[col].rolling(d).mean()

    def addExpAverage(self, s=10, col='Close'):
        '''
            Add Exponential Average Column in dataframe
            s: Number of days to span a positive integer
            col: Data set column for moving average needed Default 'Close'
            Description : n exponential moving average (EMA) is a type of
            moving average (MVA) that places a greater weight and significance
            on the most recent data points.The exponential moving average is
            also referred to as the exponentially weighted moving average
            Requisite data is available
        '''
        if not isinstance(s, int) or s < 1:
            raise ValueError("s: Span must be positive Number")
        self.data["EMA"] = self.data[col].ewm(span=s, adjust=False).mean()

    def printminima(self):
        '''
            Print Minima of every column
        '''
        print('Over all Minimum value in every Column')
        print(self.data.min())

    def drawvolatilitygraph(self):
        '''
            Draw Volatility Graph
        '''
        # Get Standrard Deviation
        self.addlogreturns()
        sdev = self.data["Log Returns"].std()
        volatility = sdev*(self.NUMOFTD**.5)
        print("Stnd, Dev: {0} Volatility: {1}".format(sdev, volatility))
        vltstr = str(round(volatility, 4)*100)
        fig, ax = plt.subplots()
        ax.set_xlabel('Log Return')
        ax.set_ylabel('Freq of Log return')
        ax.set_title('AAPL volatility: '+vltstr)
        self.data["Log Returns"].plot.hist(
                ax=ax, bins=50, alpha=0.6, color='b')

    def drawavggraph(self):
        '''
            Draw Moving and Exponential Moving Average Graph
        '''
        self.addMovingAverage(d=12, col='Close')
        self.addExpAverage(s=10, col='Close')
        fig, ax = plt.subplots()
        ax.set_title("Moving Average and Exponential Moving Average")
        self.data[['MVA', 'EMA']].plot(ax=ax)
        plt.show()

    def drawavggraphL(self, ils):
        '''
            Draw Moving and Exponential Moving Average Graph
            ils: Starting Row Index
        '''
        self.addMovingAverage(d=12, col='Close')
        self.addExpAverage(s=10, col='Close')
        fig, ax = plt.subplots()
        ax.set_title("Moving Average and Exponential Moving Average")
        self.data[['MVA', 'EMA']].iloc[ils:].plot(ax=ax)

    def drawactavggraphL(self, col='Close', ils=50):
        '''
            Draw Actual, Moving and Exponential Moving Average Graph
            col: Actual Data column default is close
            ils: Starting Row Index e.g 50
        '''
        self.addMovingAverage(d=12, col='Close')
        self.addExpAverage(s=10, col='Close')
        fig, ax = plt.subplots()
        ax.set_title("Actual, Moving Average and Exponential Moving Average")
        self.data[['MVA', 'EMA']].iloc[ils:].plot(ax=ax)
        self.data[[col]].iloc[ils:].plot(ax=ax, alpha=0.25, color='r')

    def macdGraph(self):
        '''
            MACD, MACD, short for moving average convergence/divergence, is a
            trading indicator used in technical analysis of stock prices.
            The MACD indicator(or "oscillator") is a collection of three time
            series calculated from historical price data, most often the
            closing price. These three series are: the MACD series proper,
            the "signal" or "average" series, and the "divergence" series which
            is the difference between the two

            Calculation
                MACD=12-Period EMA-26-Period EMA
                Singal line 9 - period EMA of MACD
        '''
        exp1 = self.data['Close'].ewm(span=12, adjust=False).mean()
        exp2 = self.data['Close'].ewm(span=26, adjust=False).mean()
        self.data['MACD'] = exp1-exp2
        self.data['Signal Line'] = self.data['MACD'].ewm(
                span=9, adjust=False).mean()
        fig, ax = plt.subplots()
        ax.set_title("MACD Graph")
        self.data[['MACD', 'Signal Line']].plot(ax=ax)
        self.data['Close'].plot(ax=ax, alpha=0.25, secondary_y=True, color='r')
        self.data[['MACD', 'Signal Line']].plot(ax=ax)
        self.data['Close'].plot(ax=ax, alpha=0.25, secondary_y=True, color='r')

    def sochasticoscGraph(self):
        '''
        Sochastic oscillator:A stochastic oscillator is a momentum indicator
        comparing a particular closing price of a security to a range of its
        prices over a certain period of time. The sensitivity of the oscillator
        to market movements is reducible by adjusting that time period or by
        taking a moving average of the result.It is used to generate overbought
        and oversold trading signals, utilizing a 0–100 bounded range of
        values.

        Calculation
        14-high: Maximum of last 14 trading days
        14-low: Minimum of last 14 trading days
        %K: (last close-14-low)*100/(14-high-14-low))
        %D: Simple Moving Average of %K (preferable 3 days)
        '''
        # Sochastic oscillator
        high14 = self.data['High'].rolling(14).max()
        low14 = self.data['Low'].rolling(14).min()
        self.data['%K'] = (self.data['Close']-low14)*100/(high14-low14)
        self.data['%D'] = self.data['%K'].rolling(3).mean()

        fig, ax = plt.subplots()
        ax.set_title("Sochastic oscillator")
        self.data[['%K', '%D']].iloc[3*len(self.data)//4:].plot(ax=ax)
        ax.axhline(80, c='r', alpha=0.3)
        ax.axhline(20, c='r', alpha=0.3)
        self.data[['Close']].iloc[3*len(self.data)//4:].plot(
                ax=ax, alpha=0.3, secondary_y=True)


if __name__ == "__main__":
    config = RawConfigParser()
    config.read('fin.properties')
    ta = TechAnalysis(cfg=dict(config.items('FIN')))
    ta.addDailyChange()
    ta.addpchange()
    ta.addnormalize()
    ta.printminima()
    print('Minimum value in every Column and index')
    print('daily_ch minimum :', ta.data['daily_ch'].min(),
          ' and index:', ta.data['daily_ch'].min())
    print('Over all Maximum value in every Column')
    print(ta.data.max())
    print('Close Maximum :', ta.data['Close'].max(), ' and index:',
          ta.data['Close'].idxmax())
    print('Close Maximum :', ta.data['Close'].max(), ' and index:',
          ta.data['Close'].idxmax())
    ta.drawvolatilitygraph()
    ta.drawavggraph()
    ta.drawavggraphL(ils=len(ta.data)//2)
    ta.drawactavggraphL(ils=len(ta.data)//2)
    ta.macdGraph()
    ta.sochasticoscGraph()
    print(ta.data.head())
