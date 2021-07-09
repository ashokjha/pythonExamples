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

def getsecondmax(dct):
    keys= list(dct.keys())
    keys.sort()
    return  keys[-2]

def getduplicates(dct):
    dpl=[]
    for itm in dct.items():
        if itm[1] > 1 :
            dpl.append(itm[0])
    return dpl

def gethighestFreq(dct,dpl):
    freq = 0
    num = -1
    for itm in dpl:
        print(itm)
        if(dct[itm] > freq):
            freq = dct[itm]
            num = itm
            print(freq,num)
    return num,freq


data = eval(input("Enter a List: "))
ll=[]
for d in data:
    ll.append(int(d))

dct = {}
for d in ll:
    dct[d] = dct.get(d, 0) + 1

print("Output:")
print("Second Maximum number: ", getsecondmax(dct))

dpl=getduplicates(dct)
print('Duplicate Numbers:',dpl)
num,freq = gethighestFreq(dct,dpl)
print('{0} having highest frequency which is {1}.'.format(num,freq))
        
    


