'''
1. Write a program to take input of two lists from user and perform the following operations:
(i) Display the list having maximum number of elements.
(ii) Display union of two lists.
(iii) Display intersection of two lists.
Example:
Enter First List:[2,3,4,5,6,7]
Enter Second List:[4,5,6,7,8,9,10]
Output:
[4,5,6,7,8,9,10]
Union:[2,3,4,5,6,7,8,9,10]
Intersection:[4,5,6,7]
'''
ll1 = eval(input("Enter First List: "))
ll2 = eval(input("Enter Second List: "))
print("Output:")
if len(ll1) >= len(ll2):
    print(ll1)
else:
    print(ll2)
# Union
lu=ll1[:]
for d in ll2:
    if(d not in lu):
        lu.append(d)
print("Union:",lu)

# Intersection
li=ll1[:]
for d in ll1:
    if(d not in ll2):
        li.remove(d)
print("Intersection:",li)
