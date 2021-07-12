numList = eval(input())
sumEven=0
cntOdd=0
for i in numList:
      if i%2==0:
            sumEven += i**2
      else:
            cntOdd+=1
print(sumEven)
print(cntOdd)
      
