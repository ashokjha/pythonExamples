n = input()
count = 0
l1 = n.split(" ") 
for x in l1: 
      if x.lower() == x.lower()[::-1]:
            print(x)
            count += 1
print ("No of Palindrome word : ",count)
