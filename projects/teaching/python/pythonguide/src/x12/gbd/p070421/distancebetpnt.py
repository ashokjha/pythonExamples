# -*- coding: utf-8 -*-

import math

def distancebtweentwopoint(p1,p2):
    distance = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2) 
    return distance


if __name__ == '__main__':
    p1 = eval(input())
    p2 = eval(input())
         
    print(distancebtweentwopoint(p1,p2))
