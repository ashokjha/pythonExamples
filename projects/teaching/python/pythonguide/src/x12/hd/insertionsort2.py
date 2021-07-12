n=int(input())
lst=[]

for i in range(n):
      elm=int(input())
      lst.append(elm)
print(lst)      
for i in range(1,len(lst)):
      cval= lst[i]
      pos=i
      while pos>0 and lst[pos-1]%10>cval%10:
            lst[pos]=lst[pos-1]
            pos = pos-1
      lst[pos]=cval
print(lst)      


