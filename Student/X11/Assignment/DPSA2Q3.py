inpt=int(input("Please enter a number : "))
a=0
b=1
if(inpt == a):
      print(inpt," is from Fibonacci Series ")
elif(inpt == b):
      print(inpt," is from Fibonacci Series ")
else:
      i=a+b
      while(i<=inpt):
            if(i==inpt):
                  print(inpt," is from Fibonacci Series ")
                  break
            else:
                  a=b
                  b=i
                  i=a+b
      else:
            print(inpt," is not from Fibonacci Series ")


