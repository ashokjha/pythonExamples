'''
4. Write a Python program to remove duplicate words
    from a given string and display the resultant string in ascending order.
Original String:
Next Time There Won't Be A Next Time
Output:
A Be There Won't    
'''
orgs = input("Original String:\n")
orgsl = orgs.split()
dct = {}
for d in orgsl:
     if(orgs.count(d)>1):
         orgs = orgs.replace(d,'')

orgsl = orgs.strip().split()
orgsl.sort()
revs=" ".join(orgsl)
print("Output:",revs,sep='\n')