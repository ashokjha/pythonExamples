def power(b,p):
    '''
       b^p : Base to power exponent (p)
       b: is real
       p: power whole  number
    '''
    if p==1:
        return b
    else:
        return b*power(b,p-1)

print(power(1.2,8))