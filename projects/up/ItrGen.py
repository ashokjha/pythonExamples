# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 20:42:47 2021

@author: Ashok Kumar Jha
"""

import pandas as df


# traditional


def factors(n):
    '''
     Returns factors of number

     n Number for which factors required
    '''
    results = []  # store factors in a new list
    for k in range(1, n+1):
        if n % k == 0:  # divides evenly, thus k is a factor
            results.append(k)  # add k to the list of factors
    return results


# Generator


def factorsgen(n):
    '''
     Generate factors of number and return one by one in order

     n Number for which factors required
    '''
    for k in range(1, n+1):
        if n % k == 0:  # divides evenly, thus k is a factor
            yield k  # yield this factor as next result


def factorsEfficient(n):  # generator that computes factors
    '''
     Generate factors of number and yield in efiicientv way

     n Number for which factors required
    '''

    f = 1
    while f**2 < n:  # while f**2 < n
        if n % f == 0:
            yield f
            yield n // f
        f += 1
    if f**2 == n:  # special case if n is perfect square
        yield f


def fibo(stop=500):
    '''
        Generate Fibonaci number from 0 and reurns in fast way

        Stop : Fibonaccy number <= stop
        Assumption: Stop >0
    '''
    f, s = 0, 1
    while True:
        yield f
        f, s = s, f+s
        if f > stop:
            break


if __name__ == '__main__':
    # Iterator
    # From Iterator
    for i in range(10):
        print(i)

    print('Factor of 100 ')
    for i in factors(100):
        print(i)

    print('Factor Generator in increasong order of 100 ')
    for i in factorsgen(100):
        print(i)
    print('Efficient Factor Generator')
    for i in factorsEfficient(100):
        print(i)

    print('FIBO')
    for i in fibo(1000):
        print(i)

    dfo = df.DataFrame({'S.No': [1, 2, 3], 'name': [
                       'sapan', 'vivek', 'vishal']})
    dfo.rename(columns={'S.No': 'SNo', 'name': 'Sname'})
    dfo.index = {1, 2, 3}
    print(dfo)
    print(123)
