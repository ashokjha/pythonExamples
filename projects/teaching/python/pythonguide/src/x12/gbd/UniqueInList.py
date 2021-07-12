def Unqlist(lst):
    '''
        Returns unique elements in list
    '''   
    '''
        unql = []
        for elm in lst:
            if lst.count(elm) == 1:
                unql.append(elm)
        return unql
    '''
    return [elm for elm in lst if lst.count(elm)==1]

print("Input")           
ul = eval(input())
unq = Unqlist(ul)
print("Output")
print(unq)            
    