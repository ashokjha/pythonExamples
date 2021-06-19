tup1 = eval(input("Enter first Tupple : "))
tup2 = eval(input("Enter second Tupple :  "))
res = tuple(set(tup1+tup2))
print("Union: " + str(res))
