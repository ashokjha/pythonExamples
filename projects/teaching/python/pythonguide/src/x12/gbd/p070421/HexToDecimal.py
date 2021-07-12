# -*- coding: utf-8 -*-

def hextodecimal(hexnumstr):
    ps = len(hexnumstr)-1
    cnt = 0
    for i in range(2,len(hexnumstr)):
        v = hexnumstr[i]
        if v >= '0' and v <= '9':
            rem = int(v)
        elif v >='A' and v <= 'F':
            rem = ord(v) - 55
        elif v >= 'a' and v <= 'f':
            rem = ord(v) - 87
        cnt = cnt + (rem * (16 ** (ps-i)))   
        
    return cnt
       

hex = input(" ")
cint = hextodecimal(hex)

print(cint)

