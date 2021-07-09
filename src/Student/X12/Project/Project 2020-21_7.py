d1 = eval(input("Dictionary 1: "))
d2 = eval(input("Dictionary 2: "))
d3 = {}
for i in d1:
    if i in d2:
        d3[i] = d2[i] - d1[i]
print(d3)
