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
import ReadYFinance as ryf


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
            self.data = pd.read_csv(TechAnalysis.DATA_FILE, index_col=0,
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
        self.data["MvA"] = self.data[col].rolling(10).mean()

    def addExpAverage(self, s=10, col='Close'):
        '''
            Add Exponential Average Column in dataframe
            s: Number of days to span a positive integer
            col: Data set column for moving average needed Default 'Close'
            Description : n exponential moving average (EMA) is a type of
            moving average (MA) that places a greater weight and significance
            on the most recent data points.The exponential moving average is
            also referred to as the exponentially weighted moving average
            Requisite data is available
        '''
        if not isinstance(s, int) or s < 1:
            raise ValueError("s: Span must be positive Number")
        self.data["EMvA"] = self.data[col].ewm(span=10, adjust=False).mean()

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
        self.data[['MvA', 'EMvA']].plot(ax=ax)
        plt.show()

    def drawavggraphL(self, ils=50):
        '''
            Draw Moving and Exponential Moving Average Graph
            ils: Starting Row Index e.g 50
        '''
        self.addMovingAverage(d=12, col='Close')
        self.addExpAverage(s=10, col='Close')
        fig, ax = plt.subplots()
        ax.set_title("Moving Average and Exponential Moving Average")
        self.data[['MvA', 'EMvA']].iloc[ils:].plot(ax=ax)

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
        self.data[['MvA', 'EMvA']].iloc[ils:].plot(ax=ax)
        self.data[[col]].iloc[ils:].plot(ax=ax, alpha=0.25)


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
    ta.drawavggraphL(ils=60)
    ta.drawactavggraphL()
    print(ta.data.head())
