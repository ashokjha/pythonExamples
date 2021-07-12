number = int(input(" Please Enter a Number: "))
i = 1
sum = 0
while(i < number):
    if(number % i == 0):
        sum = sum + i
    i = i + 1
if (sum == number):
    print(" %d is a Perfect Number" %number)
else:
    print(" %d is not the Perfect Number" %number)


