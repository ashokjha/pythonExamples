# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 18:22:34 2021

@author: Ashok Kumar JHa
"""
import xlsxReportWriter as xrw

xrw = xrw.xlsxReportWriter()
xrw.createData()
print(xrw.data.tail())
xrw.resizeData()
print(xrw.data.tail())
xrw.createma10Chart()
xrw.createmacdChart()
xrw.createsochasticChart()
xrw.clean()
