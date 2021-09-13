# -*- coding: utf-8 -*-.

"""
Created on Sun Jun 27 12:41:22 2021
DataFrame
@author: Ashok KumarJha
"""

import pandas as pd

# Reading the CSV, Setting Index to First column of CSV, Changeing Data
# type of Index to DateTime
data = pd.read_csv("data/AAPL.csv", index_col=0, parse_dates=True)


print(data.dtypes)

# Head Location
print(data.head())
# Tail Location
print(data.tail())

# Getting data at location  at 2020-06-30
print(data.loc['2020-06-30'])

# Getting data at 3 rd location i.e loc 2020-07-02
print(data.iloc[3])

# Getting last data
print(data.iloc[-1])

# Getting last data in range
print(data.iloc[3:8])

# Getting last data in range
print(data.loc['2021-06-21':])

# Getting last data in range
print(data.loc[:'2020-07-21'])

# Getting last data in range
print(data.loc['2020-07-21':'2021-01-01'])
