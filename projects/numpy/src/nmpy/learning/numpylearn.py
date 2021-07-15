# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 23:13:58 2021

@author: USER
"""

import numpy as np


print(np.__version__)

def defining():
    onedr = np.array([1.1,2.0,3.2])
    twodr = np.array([(1,2,3),
                      (4,5,6)])
    threedr = np.array([
        [[1, 2,3],
            [4, 5, 6]],
        [[7, 8,9],
            [10, 11, 12]]
    ])
    print(('onedr shape = {} dtype ={} \ntwodr shape = {} dtype ={} \n'
           + 'threedr   shape = {} dtype ={} ').format(onedr.shape, onedr.dtype, 
                             twodr.shape, twodr.dtype, threedr.shape, 
                             threedr.size))
    print('onedr = {} \ntwodr= {} \nthreedr  = {} '.format(onedr,twodr,threedr))
    
def zerros():
    nzr = np.zeros((2,2))
    print(nzr)
    nzr1=np.zeros((2,3,4), dtype=np.int16)
    print(nzr1)

def ones():
    nor = np.ones((2,2))
    print(nor)
    nor1=np.ones((2,3,4), dtype=np.int16)
    print(nor1)

def reshaping():
    arr = np.array([
        [[1, 2,3],
            [4, 5, 6]],
        [[7, 8,9],
            [10, 11, 12]]])
    print(arr)
    print(arr.shape)
    arr1 = arr.reshape((6,2))
    print(arr1.shape)
    print(arr1)
    
    arr2 = arr.reshape((12,))
    print(arr2.shape)
    print(arr2)
    
def flatternEx() :
    arr = np.array([
        [[1, 2,3],
            [4, 5, 6]],
        [[7, 8,9],
            [10, 11, 12]]])
    print("Arr = ",arr)
    print("Arr.flattern() =",arr.flatten())     
    
def hvstackEx():
    '''
    Horrizonatl stacking 
    The arrays must have the same shape along all but the second axis, 
    except 1-D arrays which can be any length.
    Vertical stacking
    The arrays must have the same shape along all but the first axis. 
    1-D arrays must have the same length.
    Returns
    -------
    None.

    '''
    arr1=[[1,2,3,4,5],[6,7,8,9,10]]
    arr2=[[11,12,13,14,15],[16,17,18,19,20]]
    print("Ar1 = ",arr1)
    print("Ar2 = ",arr2)
    print("np.hstack((Arr1,Arr2)) = \n",np.hstack((arr1,arr2)))

def randomexgassim():
    '''
        Sample for using random
        To generate random numbers for Gaussian distribution use
    
        numpy.random.normal(loc, scale, size)
        
        Here
        
        Loc: the mean. The center of distribution
        scale: standard deviation.
        Size: number of returns
    '''
    ## Generate random nmber from normal distribution
    normal_array = np.random.normal(5, 0.5, 10)
    print(normal_array)
    
    
    
if __name__ == '__main__':
    # defining()
    # zerros()
    # ones()
    # reshaping()
    # flatternEx()
    # hvstackEx()
    randomexgassim()

