# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 21:05:18 2021

@author: Ashok Kumar Jha
"""


def binary_search(data, searchterm):
    '''
    Return index of search term in given data

    Parameters
    ----------
    data : sorted list

    Search_Term : search term
        

    Returns
    -------
    index number

    '''
    n = len(data)
    L = 0
    R = n-1
    
    while L <= R:
        mid = (L+R)//2
        if data[mid] < searchterm:
            L = mid + 1
        elif data[mid] > searchterm:
            R = mid - 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    # Insert your array here
    ll = [1,2,3,4,7,9,12,14,18]
    # term to be searched
    term = 14
    index = binary_search(ll, term)
    if index >= 0:
        print("{} is at index {}".format(ll[index], index))
    else:
        print("Search term not found")