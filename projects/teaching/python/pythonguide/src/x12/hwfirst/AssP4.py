'''
4. Write a Python program to remove duplicate words
    from a given string and display the resultant string in ascending order.
Original String:
Next Time There Won't Be A Next Time
Output:
A Be There Won't    
'''

def removedplAndsort(line, des=True):
    words = line.split()
    uword = []
    for d in words:
         if d not in uword and words.count(d)==1:
             uword.append(d)
    
    uword.sort()
    return " ".join(uword)
    
orgs = input("Original String:\n")

print("Output:",removedplAndsort(orgs))