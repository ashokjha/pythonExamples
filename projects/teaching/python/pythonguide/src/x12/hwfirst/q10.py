d={}
d[1]=3
d['1']=2
d[1.0]=4
s=0
for k in d:
    s+=d[k]
print(s)