'''
2. Write a program to take input of a list from user and perform the following operations:
(i) Display the second maximum number from the list.
(ii) Display duplicate numbers from the list.
(iii) Display the highest frequency number with its frequency from the list.
Example:
Enter a List:[2,3,4,5,6,7,3,4,7,4]
Output:
Second Maximum number: 6
Duplicate Numbers: [3,4,7]
4 having highest frequency which is 3.
'''
data = eval(input("Enter a List: "))
ll=[]
for d in data:
    ll.append(int(d))

dct = {}
for d in ll:
    dct[d] = dct.get(d, 0) + 1
keys= list(dct.keys())
keys.sort()
print("Output:")
print("Second Maximum number: ", keys[-2])
freq = 0
num = -1
dpl=[]
for itm in dct.items():
    if itm[1] > 1 :
        dpl.append(itm[0])
        
    if(itm[1] > freq):
        freq = itm[1]
        num = itm[0]

print('Duplicate Numbers:',dpl)
print('{} having highest frequency which is {}.'.format(num,freq))
        
    


