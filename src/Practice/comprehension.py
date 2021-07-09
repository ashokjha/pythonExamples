# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 20:37:54 2021

@author: Ashok Kumar Jha
"""
import ItrGen

n=10
lst1 = [ k*k for k in range(1, n+1) ] #list comprehension
set1 = { k*k for k in range(1, n+1) } #set comprehension
tpl1 = ( k*k for k in range(1, n+1) ) #generator comprehension
dct1= { k:k*k for k in range(1, n+1) } #dictionary comprehension

print('From List Comprension ')
print(lst1)

print('From Set Comprension ')
print(set1)

print('From Touple Comprension ')
print(tpl1)

print('From Dictionary Comprension ')
print(dct1)
ItrGen.factors(100)