# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 20:01:30 2021

@author: Ashok Kumar Jha
"""


from pandas_datareader import data as pdr

from datetime import datetime as dt


def getYFData(cfg):
    '''
       Get Yahoo Finance Data
    '''
    ticker = cfg['ticker']
    start_date = dt.strptime(cfg['sd'], cfg["date-format"])
    end_date = dt.strptime(cfg['ed'], cfg["date-format"])
    return pdr.get_data_yahoo(ticker, start_date, end_date)


if __name__ == '__main__':
    dct = {'DATE-FORMAT': '%d/%m/%Y', 'SD': '1/1/2020', 'ED': '31/12/2021',
           'TICKER': 'AAPL'}
    print(getYFData(dct))
