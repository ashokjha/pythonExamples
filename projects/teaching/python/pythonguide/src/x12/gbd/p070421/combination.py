# -*- coding: utf-8 -*-

def combination(n):
    if n==0:
        return 1
    else: 
        return n*combination(n-1)

ll = eval(input()) 
print(combination(len(ll)))
