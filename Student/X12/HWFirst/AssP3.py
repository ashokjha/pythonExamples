'''
Write a program to take input of a list from user and perform the following operations:
(i) Display the list in reverse order.
(ii) Display each number along with its frequency.
(iii) Display the updated list after swapping first half with second half.
      For odd number of elements, the position of the middle
      
'''
ol = eval(input("Enter a List: "))

print("Output:")
#Reverse
rl=ol[-1::-1]

print("Reverse List: ", rl)

pos=len(rl)//2

dct = {}
for d in ol:
     dct[d] = dct.get(d, 0) + 1
print("Number\tFrequency")   
for itm in dct.items():
    print(itm[0],'\t',itm[1])

length=len(rl)
pos = length//2
ul=[]
if(length % 2 ==0):
    ul = ol[pos:]+ol[0:pos]  
else:
    ul = ol[pos+1:]+[ol[pos]]+ol[:pos]
print("Updated List: ",ul)    
