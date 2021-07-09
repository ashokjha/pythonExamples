
import math
r = int(input("Please enter radius of cylinder "))
h = int(input("Please enter height of cylinder "))
v = math.pi*r**2*h
A = 2*math.pi*r*h + 2*math.pi*r*2

print("Volume of cylinder = %.2f"%(v))
print("Total Surface area of cylinder = %.2f"%(A))