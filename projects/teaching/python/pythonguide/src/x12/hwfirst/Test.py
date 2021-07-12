'''
Sum of AP
ft: first term
cr: Common Differe3nce
nt: Number Of Term
S = (n/2)*[2*ft + (nt-1)*cd]
'''
def sumofAP(ft,cd,nt):
    return (nt/2)*(2*ft + (nt-1)*cd)
'''
Sum of GP
ft: first term
cr: Common Ratio
nt: Number Of Term
S = a*[(r^n-1)/(r-1)]
'''
def sumofGP(ft,cr,nt):
    return ft*((cr**nt - 1)/(cr-1))


print("Sum of AP with First Term = ",123," Common Diff = ",48," Num of Term= ",87, " = ", sumofAP(123,48,87))

print("Sum of GP with First Term = ",12," Common Ratio = ",7.5," Num of Term= ",10, " = ", sumofGP(12,7.5,10))