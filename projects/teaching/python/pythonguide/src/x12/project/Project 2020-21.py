# Looping Programs
# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
# variable to store the sum
sum = 0
# iterate over the list
for val in numbers:
      sum = sum+val
print("The sum is", sum)

# Series Program
# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

#Pattern Programs
#Downward Triangle Pattern of Stars
rows = int(input(" Enter +ve number  : "))

k = 2 * rows - 2

for i in range(rows, -1, -1):

    for j in range(k, 0, -1):

        print(end=" ")

    k = k + 1

    for j in range(0, i + 1):

        print("*", end=" ")

    print("")


