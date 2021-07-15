# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 13:09:30 2021

@author: USER
"""

class tvm(object):
    def __init(self,rate,period):
        self.rate = rate
        self.acp = period
        
    def tvm(self,amt,time): 
        return amt*(1+self.rate)**time