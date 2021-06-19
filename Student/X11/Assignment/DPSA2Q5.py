inpt=5
k =  2*inpt-2
print(k)
for i in range(0,inpt):
	for j in range(0,k):
	    print(end=" ")
	k=k-1
	#print(k)
	for j in range(0,i+1):
	    print("* ",end="")
	print("\r")
k = inpt-2
#print(k)
for i in range(inpt,-1,-1):
	for j in range(k,0,-1):
		print(end=" ")
	k=k+1
	#print(k)
	for j in range(0,i+1):
		print("* ",end="")
	print("\r")
