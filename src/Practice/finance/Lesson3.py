# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 13:51:19 2021
Technical Analysis
Calculate with Column
 Add Column
 Drop Column
 min, max,argmin (Deprecated instead use idxmin),
  argmax(deprecated instead use idxmax)
 Mean
@author: Ashok Kumar Jha
"""

from TechAnalysis import TechAnalysis


ta = TechAnalysis()
ta.addDailyChange()
ta.addpchange()
ta.addnormalize()
ta.printminima()
print('Minimum value in every Column and index')
print('daily_ch minimum :', ta.data['daily_ch'].min(),
      ' and index:', ta.data['daily_ch'].min())
print('Over all Maximum value in every Column')
print(ta.data.max())
print('Close Minimum :', ta.data['Close'].min(), ' and index:',
      ta.data['Close'].argmin())
print('Close Maximum :', ta.data['Close'].max(), ' and index:',
      ta.data['Close'].argmax())
ta.drawvolatilitygraph()
ta.drawavggraph()
ta.drawavggraphL(ils=60)
ta.drawactavggraphL()
print(ta.data.head())
