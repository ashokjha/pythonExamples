#  Q1
print('\nAnswer of Q1: ')
def changer(p,q=10):
    p = p/q
    q = p%q   
    print(p,"#",q)
    return(p)

a = 200
b = 20
a = changer(a,b)

print(a,"$",b)

#  Q 2
print('\nAnswer of Q2: ')
def func(L):
    Times = 0
    Alpha = ""
    Add = 0
    for c in range(1,6,2):
        Times = Times + c   # 0->1->4-> 9
        Alpha = Alpha + L[c-1] + "$" # ""-> P$->P$R$ -> P$R$S$
        Add = Add + L[c]    # 0->20-> 30-> 60
    print(Times,Add,Alpha)

Data=["P",20,"R",10,"S",30]

func(Data)

#  Q 3
print('\nAnswer of Q 3: ')

def fun():
    l1=["Apple","Berry","Cherry","Papaya"]
    l2=l1
    l3=l1[:]
    l2[0]="Guava"
    l2[1]="Kiwi"
    sum=0
    for l in (l1,l2,l3):
        if l[0]=="Guava":
            sum += 1   
        if l[1]=="Kiwi":
            sum= sum+20
    print(sum)
# As below code is not present in assignment so no ouput

fun()

#  Q 4
print('\n Answer of Q 4: ')

def dothis(x,I=[]):
    for i in range(x):
        I.append(i*i)
    print(I)

dothis(2)
dothis(3,[3,2,1])
dothis(3)


#  Q 5
print('\nAnswer of Q5: ')

def add(x,y,z):
    print(x+y+z)
    
def prod(x,y,z):
    return(x*y*z)

a=add(6,16,26)
b=prod(2,3,6)
print(a,b)

#  Q 6
print('\nAnswer of Q6: ')
x=5
def func2():
    global x
    x=x+1
    print (x)

func2()
print(x)

#  Q 7
print('\nAnswer of Q 7: ')
def Findoutput():
    L = "earn"
    x = ""
    count = 1
    for i in L:
        if i in ['a', 'e',' i', 'o', 'u']:
            x = x+i.upper()
        else:
            if count % 2 != 0:
                x = x + str (len (L[:count]))
            else:
                x = x + i
                count = count + 1
    print (x)

Findoutput ()

#  Q 8
print('\nAnswer of Q 8: ')
d={}
d[1]=3
d['1']=2
d[1.0]=4
s=0
for k in d:
    s+=d[k]
print(s)
