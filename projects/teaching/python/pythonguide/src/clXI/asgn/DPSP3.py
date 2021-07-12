
nu=int(input("Please enter a positive number : "))
nbs = 3*nu -2
for i in range(nu,-1,-1):
      print(" "*nbs,end=" ")
      nbs += 1
      print("*  "*i, end=" ")
      print("\r")



