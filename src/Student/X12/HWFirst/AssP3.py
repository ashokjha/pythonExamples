'''
Write a program to take input of a list from user and perform the following operations:
(i) Display the list in reverse order.
(ii) Display each number along with its frequency.
(iii) Display the updated list after swapping first half with second half.
      For odd number of elements, the position of the middle
      
'''

def reveselist(ll):
    return ll[-1::-1]

def freqTable(ll) :
    dct = {}
    for d in ol:
        dct[d] = dct.get(d, 0) + 1
    return dct

def swaplist(ol):
    length=len(ol)
    pos = length//2
    ul=[]
    if(length % 2 ==0):
        ul = ol[pos:]+ol[0:pos]  
    else:
        ul = ol[pos+1:]+[ol[pos]]+ol[:pos]
    return ul

ol = eval(input("Enter a List: "))

#Reverse
print("Reverse List: ",reveselist(ol))

dct=freqTable(ol)
print("Number    Frequency")   
for itm in dct.items():
    print('  ',itm[0],'   \t',itm[1])

print("Updated List: ",swaplist(ol))  

