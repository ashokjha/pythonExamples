n=int(input())
lst=[]

for i in range(n):
      felm=input()
      selm=int(input())
      lst.append([felm,selm])
print(lst)      
for i in range(1,len(lst)):
      cval= lst[i]
      pos=i
      while pos>0 and lst[pos-1][1]>cval[1]:
            lst[pos]=lst[pos-1]
            pos = pos-1
      lst[pos]=cval
print(lst)      


