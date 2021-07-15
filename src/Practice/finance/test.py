# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 20:01:30 2021

@author: Ashok Kumar Jha
"""


from pandas_datareader import data as pdr

import datetime as dt


def getYFData(cfg):
    '''
       Get Yahoo Finance Data
    '''
    ticker = cfg['ticker']
    start_date = dt.strptime(cfg['SD'], cfg["DATE-FORMAT"])
    end_date = dt.strptime(cfg['ED'], cfg["DATE-FORMAT"])
    return pdr.get_data_yahoo(ticker, start_date, end_date)






import pandas_datareader as pdr
import datetime as dt
 
ticker = "AAPL"
start = dt.datetime(2019, 1, 1)
end = dt.datetime(2020, 12, 31)
 
data = pdr.yahoo.daily.YahooDailyReader(ticker)
print(data.read())
