
def union(lst1,lst2):
    lst=lst1[0:]
    for i in lst2:
        if i not in lst:
            lst.append(i)
    return lst

def intersection(lst1,lst2):
    lst=[]
    for i in lst1:
        if i in lst2:
            lst.append(i)
    return lst

print ("Input")
ll1 = eval(input())
ll2 = eval(input())
print("Output")
print('Union',union(ll1,ll2))
print('Intersect',intersection(ll1,ll2))