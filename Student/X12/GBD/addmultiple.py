def addmult(l):
    '''
    Return sum of even element of list and odd elemetns of list and returns
    '''
    sumeven = 0
    sumodd = 0
    for i in range(len(l)):
        if (l[i] % 2 == 0):
           sumeven = sumeven + l[i]
        else:
           sumodd = sumodd + l[i]
    return sumeven,sumodd

print("Input")           
ul = eval(input())
r = addmult(ul)
print("Output")
print(r)            
    