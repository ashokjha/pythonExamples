import random
A=[60,50,40,30,20,10]
L=random.randint(1,3)
U=random.randint(2,4)
for i in range(L,U+1):
    print(A[i],end="#")
    
print()

'''
def func(a):
    s,m,n = 0,0,0
    for i in (0,a):
        if i%2 == 0:
            s=s+1
        elif i%5 == 0:
            m=m+2
        else:
            n=n+i
    print(s,m,n)

func(15)
'''

def story(a,b=10):
    a=a*5
    b=a//b
    print(a,"*",b)
    return(a)
x=500
y=50
x=story(x,y)
print(x,"$",y)