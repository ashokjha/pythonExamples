'''
6. Write a program to take input of two dictionaries from user and perform the following operations:
(i) Display ad of two dictionaries.
(ii) Display difference of two dictionaries.
Example:
Enter First dictionary: dict1 = {'a': 10, 'b': 5, 'c': 3}
Enter Second Dictionary: dict2 = {'d': 6, 'c': 3, 'b': 8}
Output:
Addition: {'a': 10, 'b': 13, 'c': 6,’d’: 6}
Subtraction: {‘a’:10,‘ b': 3, 'c': 0,’d’:6}
'''


def addct(d1,d2) :
    add = {}
    print(d1)
    print(d2)
    for k,v in d1.items():
        add[k]=v
    for k,v  in d2.items():
        add[k] = add.get(k,0) + v 
    return add
    
def diffdct(d1,d2) :
    dff = {}
    for k,v in d1.items() :
        dff[k]=v
    for k,v in d2.items():
        dff[k] = abs(dff.get(k,0)-v) 
    return dff



dict1 = eval(input("Enter First Dictionary: ")) 
dict2 = eval(input("Enter Second Dictionary: "))

print(addct(dict1,dict2))

print(diffdct(dict1,dict2))    
