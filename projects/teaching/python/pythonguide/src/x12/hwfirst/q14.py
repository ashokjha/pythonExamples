
def Union(L1,L2):
    res =L1.copy()
    for d in L2:
        if(d not in res):
            res.append(d)
    return res

ll1 = eval(input(" "))
ll2 = eval(input(" "))
res=Union(ll1,ll2)
print("L1=",ll1)
print("L2=",ll2)
print("Union=",res)
