
emlid = input("Please enter a email-id:")
print("User name : "+ emlid[0:emlid.index('@')])
print("Domain : "+ emlid[emlid.index('@')+1:])

