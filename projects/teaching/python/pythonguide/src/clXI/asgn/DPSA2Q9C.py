ll=[5,9,6,3,8,4,2,7]
print(ll)
mpos=len(ll)//2
m = 1
if(len(ll)%2==0):
      m=0
for i in range(mpos):
      ll[i]=ll[i]+ll[mpos+i+m]
      ll[mpos+i+m] = ll[i]-ll[mpos+i+m]
      ll[i]= ll[i]-ll[mpos+i+m] 
print(ll)
