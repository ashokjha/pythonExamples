# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 21:00:30 2021

@author: Shriyans
"""

#Types of function
# 1. Built-in functions,

#ll = input('Please enter Data') 

ll = [11,1,5,7,8,9,10]


def fun1(a,b):
    '''
    Calculate and returns summation of arguement a and arguement b 
    
    Parameters
    ----------
    a : number
        First Number.
    b : number
        Second number.

    Returns
    -------
    number
        summation.

    '''
    return a+b

def fun2(p1, p2 = 10):
    '''
    Returnmultiplication of parameter1 and parameter 2

    Parameters
    ----------
    p1 : TYPE
        DESCRIPTION.
    p2 : TYPE, optional
        DESCRIPTION. The default is 10.

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    return p1*p2


if __name__ == '__main__':

    res = fun1(2,3)
    
    
    print('fun1(2,3) = ', res)
    
    
    #res2 = fun2()
    
    
    res3 = fun2(12)
    
    res4 = fun2(8,9)
    
    res5 = fun2(p2=14, p1=5)
    
    res6 = fun2(p1=18)
    
    
    #print(" fun2() = ", res2)
    
    print(" fun2(12) = ", res3)
    
    print(" fun2(8,9) = ", res4)
    
    print("fun2(p2=14, p1=5) = ", res5)
    
    print(" fun2(p1=18) = ", res6)
    
    
    # 2. functions defined in module, 


# 3. user defined functions 