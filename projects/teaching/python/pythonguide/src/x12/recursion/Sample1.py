
def sum(n):
    '''
        Calculate sum of n natural  from 1 to n
    '''
    print(n)
    if n<=1:
        return 1
    else:
        return n+sum(n-1)
 
 
def product(n):
    '''
        Calculate sum of n natural  from 1 to n
    '''
    print(n)
    if n<=1:
        return n
    else:
        return n*product(n-1)
 



print('sum(10) = ',sum(10))
print('product(-10) = ',product(-10))



'''sum(10)=10+sum(9)=10+9+sum(8)=10+9+7+sum(6)=10+9+7+6+sum(5)=10+9+7+6+5+sum(4)=10+9+7+6+5+4+sum(3)=10+9+7+6+5+4+3+sum(2)
        =10+9+7+6+5+4+3+2+sum(1)=10+9+7+6+5+4+3+2+1 = 55
'''        
        
        
        