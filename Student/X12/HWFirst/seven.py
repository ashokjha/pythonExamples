def func(a):
    s,m,n = 0,0,0
    for i in range(0,a):
        if i%2 == 0:
            s=s+1
        elif i%5 == 0:
            m=m+2
        else:
            n=n+i
    print(s,m,n)

func(15)
