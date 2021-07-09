



ft = int(input("Enter first term : "))
cd = int(input("Enter Common difference : "))
n = int(input("Enter number of term: "))    
for i in range(1,n+1):
      print(ft+(i-1)*cd, end=' ')




num=121 #int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")

inptstr = 'A'#input("Enter a string:")

isPalindrome = False
l=len(inptstr)
for i in range(0, int(l/2)): 
      if (inptstr[i] == inptstr[l-i-1]):
            isPalindrome = True
if isPalindrome:
    print(inptstr, "is palindrome string!")
else:
    print(inptstr, "is not a palindrome  string!")
