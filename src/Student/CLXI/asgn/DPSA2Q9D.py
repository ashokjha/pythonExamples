import operator
dct={}
print(type(dct))
flg=True
while flg:
    dct[input("Please enter State: ").strip()] = input("Please enter Capital: ").strip()
    dec=(input("Please press any key to add more , to complete press exc key.: "))
    if dec=='d' or dec =='D':
        break
print(dct)
sorted_dct = dict(sorted(dct.items(), key=operator.itemgetter(1)))
print(sorted_dct)