
n = int(input("Please enter number of term : "))
sum=-1*int(n/2)
a="Series:  "
for i in range(1,n+1):
      if (i%2==0):
            a = a+str(-1*i)+'+'
      else:
            a +=str(i)
if (n%2 == 0):
      a=a.rstrip('+')
else:
      sum+=n      
print(a)
print("Sum of Series =%d"%sum)
      




