def sum(a,b): 
    return a+b

def palindrom(n,ll):
    '''
        Create n palindrome number
    '''
    for i in range(n):
       if(i==0):
           ll.append(0)
       elif(i==1):
           ll.append(1)
       else:
          ll.append(sum(ll[i-2],ll[i-1])) 

ll=[]
palindrom(10,ll)
for data in ll:
    print(data)