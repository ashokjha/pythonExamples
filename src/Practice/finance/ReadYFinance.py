# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 20:01:30 2021

@author: Ashok Kumar Jha
"""

# 
#import yfinance as yf
import pandas_datareader  as pdr

from datetime import datetime as dt
#import calendar
#import datetime
#import time


def getYFData(cfg):
    '''
       Get Yahoo Finance Data
    '''
    ticker = cfg['ticker']
    #yf.pdr_override()

    start_date = dt.strptime(cfg['sd'], cfg["date-format"])
    end_date = dt.strptime(cfg['ed'], cfg["date-format"])
    
    #st = time.strptime(cfg['sd'], cfg["date-format"])
    #ed = time.strptime(cfg['ed'], cfg["date-format"])
    
    #from_date = dt(st.tm_year,st.tm_mon,st.tm_mday)
    #to_date = dt(ed.tm_year,ed.tm_mon,ed.tm_mday)
    
    #return pdr.get_data_yahoo(ticker, start_date, end_date)  3/11/2000
    return pdr.data.get_data_yahoo(ticker)#, "2020-01-01", "2021-07-01")

    #return fyf.download(ticker, start_date, end_date)


if __name__ == '__main__':
    dct = {'date-format': '%d/%m/%Y', 'sd': '1/1/2020', 'ed': '31/12/2021',
           'ticker': 'AAPL'}
    print(getYFData(dct))
