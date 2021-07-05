# -*- coding: utf-8 -*-

def sumofdigit(num,s=0):
    if num != 0:
        s = s+(num % 10)+sumofdigit(num//10,s)
    return s

num = int(input(''))

print(sumofdigit(num,0))