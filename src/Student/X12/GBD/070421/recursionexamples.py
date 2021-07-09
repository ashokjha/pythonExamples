# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 19:29:16 2021

@author: Ashok Kumar Jha
"""

def binary_search(start,end,data,target):
    '''
    Return index of search term in given data

    Parameters
    ----------
    start : int 
        from index.
    end : int
        to index.
    data : list
        sorted list of integer.
    target : int
        element to find.

    Returns
    -------
    int
        index.

    '''
    #Condition to check if element is not present 
    if start <= end:
       mid = (start+end) // 2
     
       #Check if mid element is the target element
       if data[mid] == target:
         return mid
     
       #If not, check if lesser than mid element
       #Change range to start to mid-1, since less than mid
       elif target < data[mid]:
         return binary_search(start,mid-1,data,target)
     
       #Check if lesser than mid element
       #Change range to mid+1 to end, since greater than mid
       elif target > data[mid]:
         return binary_search(mid+1,end,data,target)
    else:
       return -1


if __name__ == '__main__':
    data = eval(input('Input list of Data : '))
    # term to be searched
    term = eval(input('Input search Element : '))
    print(type(term))
    index = binary_search(0,len(data),data, term)
    if index >= 0:
        print("{} is at index {}".format(data[index], index))
    else:
        print("Search term not found")
    
    
    
    
    #print('gcd(24,36)=',gcd(24,36))
    #print('gcd(36,24)=',gcd(36,24))    
    
    #for elm in fiboseries(20):
    #    print(elm)


def gcd(num1,num2):
    '''
    Reurns GCD of two natural number

    Parameters
    ----------
    num1 : Natural number
        1st Number .
    num2 : Natural Number
        Second Number.

    Returns
    -------
     gcd a natural number

    '''
    if num1 % num2 == 0: 
        return num2
    return gcd(num2, num1 % num2)

def sumofnatural(n=10):
    '''
    returns sum of n natural number
    required: 

    Parameters
    ----------
    n : TYPE, optional
        Natural number. The default is 10.

    Returns
    -------
    sum

    '''
    if n==1:
        return n
    return n+sumofnatural(n-1)
    

def factorial(n=10):
    '''
    returns factrial of n: 

    Parameters
    ----------
    n : TYPE, optional
        Natural number. The default is 10.

    Returns
    -------
    n! i.e factorial n

    '''
    if n in (0,1):
        return 1
    return n*factorial(n-1)
    