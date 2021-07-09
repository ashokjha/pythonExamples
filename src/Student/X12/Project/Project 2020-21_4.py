l = list(map(int, input().split()))
i = len(l)//2
a = sum(l[:i])
b = sum(l[i:])
if a > b:
    print(l[i:]+l[:i])
elif b > a:
    print(l[:i]+l[i:])
