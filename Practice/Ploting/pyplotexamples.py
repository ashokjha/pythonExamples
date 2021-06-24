# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 10:59:16 2021

@author: Ashok Kumar Jha
"""
import ChartData

from matplotlib import pyplot
import numpy as np

class graphsample:
    def __init__(self):
        '''construct
        '''
            
    def linegraph(self) :
        '''
            Draw line Graph
            Current version is sample ....
            Refact @TODO
        '''
        X=np.arange(1,20,2,np.int16)
        t=np.linspace(5,20,10)
        pyplot.plot(X,t,'rp:',label='Linear')
        pyplot.plot(X,np.log(t),'bo:',label='Log')
        pyplot.plot(X,np.sin(t),'g^:',label='sin')
        pyplot.xlabel(' Data ')
        pyplot.ylabel(' Value ')
        pyplot.title("Line/marker Graph")
        pyplot.legend(loc='upper center')
        pyplot.show()
        
    def barsample(self) :
        '''
            Draw Bar Chart
        
            Refact @TODO
        '''
        pyplot.figure(figsize=(20,20))
        pyplot.bar(ChartData.stdata,ChartData.pop, label ='Population')
        pyplot.xlabel(' State ')
        pyplot.xticks(rotation=60, ha='right')
        pyplot.ylabel(' Population in Lakhs ')
        pyplot.title("2021 estimates")

        
        pyplot.legend(loc='upper center')
        
        pyplot.show()        

gs=graphsample()
gs.linegraph()

gs.barsample()