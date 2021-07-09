# -*- coding: utf-8 -*-
i=0
s1=0
def sumofdigit(num,s=0):
    global i,s1   
    i = i+1
    s1 = s1+num % 10
    print('call {} -> {} sum = {}'.format(i,num,s1)) 
    if num != 0:
        s = s+(num % 10)+sumofdigit(num//10,s)   
    return s

num = int(input(''))

print("sumofdigit({},0)=".format(num),sumofdigit(num,0))

'''
n=234560
First Call
   s=0
   num % 10 = 234560%10=0 , 234560 // 10 = 23456 

second call : s=0, 23456%10=6 , 23456 // 10 = 2345
              s= 0+6=6
third call : s=6, 2345%10=5 , 2345 // 10 = 234
              s= 6+5=11
Fouth call : s=11, 234%10=4 , 234 // 10 = 23
              s= 11+4=15
Fith call : s=15, 23%10=3 , 23 // 10 = 2
              s= 15+3=18
sixth call : s=18, 2%10=2 , 2 // 10 = 0
              s= 18+2=20
Seventh Call  : s=20, n=0 return 20
'''
              
              