

def merge(lst1,lst2):
    for i in lst1:
        lst2.append(i)
    return lst2

ll1 = eval(input())
ll2 = eval(input())
ll1.sort()
ll2.sort()
print(ll1)
print(ll2)
merge(ll1,ll2)
ll2.sort()
print(ll2)