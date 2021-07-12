def Modify(l):
    '''
    Modify list even element by its thrice
    and odd elements by its twice value
    then prints
    '''
    for i in range(len(l)):
        if (l[i] % 2 == 0):
           l[i] = l[i]*3
        else:
           l[i] = l[i]*2
print("Input")           
a = eval(input())
Modify(a)
print("Output")
print(a)            
    
