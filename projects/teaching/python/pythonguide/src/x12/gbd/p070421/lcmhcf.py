# -*- coding: utf-8 -*-

def LCM(a, b):
    return (a*b)//HCF(a,b)

def HCF(a,b):
    if a % b == 0: 
        return b
    return HCF(b, a % b)

num1= int(input())
num2= int(input())

print("hcf ", HCF(num1,num2))

print("lcm ", LCM(num1,num2))

