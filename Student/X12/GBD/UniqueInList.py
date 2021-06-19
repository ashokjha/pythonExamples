def Unqlist(lst):
    '''
    Returns unique elements in list
    '''    
    unql = []
    for elm in lst:
        if elm  not in unql:
            unql.append(elm)
    return unql
     
print("Input")           
ul = eval(input())
unq = Unqlist(ul)
print("Output")
print(unq)            
    