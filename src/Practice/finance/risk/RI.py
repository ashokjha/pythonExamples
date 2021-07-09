# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 16:33:28 2021

@author: Ashok Kumar Jha
"""

import pandas_datareader.famafrench as ff 
import pandas_datareader.data as pdr

#import get_available_datasets
ds = ff.get_available_datasets()

for s in ds:
    data = pdr.DataReader(s,'famafrench')
    print(s)
    print(data)