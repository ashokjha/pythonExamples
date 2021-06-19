def Unqlist(lst):
    '''
    Returns duplicate elements in list
    '''    
    dpl = []
    for elm in lst:
        if lst.count(elm) >1 and elm  not in dpl:
            dpl.append(elm)
    return dpl
     
print("Input")           
ul = eval(input())
dpl = Unqlist(ul)
print("Output")
print(dpl)  