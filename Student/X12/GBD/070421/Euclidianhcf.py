# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 20:37:48 2021

@author: Ashok Kumar Jha
"""

def hcfof(num1, num2):
    '''
    GCF or GCD using Euclidian algorithm 

    Parameters
    ----------
    num1 : natural number
        first  number.
    num2 : natural number
        second number.

    Returns
    -------
    x : number
        HCF/GCD.

    '''
    while(num2):
        num1, num2 = num2, num1 % num2
    return num1

hcf = hcfof(200, 400)
print("The HCF is", hcf)
hcf = hcfof(600, 300)
print("The HCF is", hcf)