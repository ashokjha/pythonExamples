#The monthly telephone bills as per the following rule:
#Minimum Rs. 200 for upto 100 calls.
#Plus Rs. 0.60 per call for next 50 calls.
#Plus Rs. 0.50 per call for next 50 calls.
#Plus Rs. 0.40 per call for any call beyond 200 calls.
#Write a program that accepts number of calls as input. It calculates the total bill amount and
#prints the total bill amount

import math
n = int(input("Please enter no of calls : "))
totalbill=0.0
if n<=100:
    totalbill=200
elif n>100 and n <=150:
    totalbill = 200 + 0.60*(n-100)
elif n>150 and n <=200:
    totalbill = 200 + 0.60*50+0.50*(n-150)  
else:
    totalbill = 200 + 0.60*50+0.50*50+ 0.40*(n-200)
print("total bill amount = ",totalbill)