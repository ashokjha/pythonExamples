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

dict1 = eval(input("Enter First Dictionary: ")) 
dict2 = eval(input("Enter Second Dictionary: "))
print("Output:")
add = dict1.copy()
for key in dict2.keys():
    add[key] = dict1.get(key,0)+dict2.get(key,0)
print(add)
diff1=dict1.copy()
for key in dict2.keys():
    diff1[key] = abs(dict1.get(key,0)-dict2.get(key,0))
print(diff1)    
