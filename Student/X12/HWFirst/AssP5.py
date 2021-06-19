'''
5. Write a Python program to display the frequency of each letter of an input string using dictionary.
   Also display the number of vowels and consonants present in the given string.
Original String:
Alligator
Output:
A – 2
G - 1
I – 1
L – 2
O - 1
R – 1
T – 1
'''
orgs = input("Original String:\n").strip()
dct={}
for c in orgs:
         dct[c] = dct.get(c, 0) + 1
vowelcount = 0
conscont = 0

for item in dct.items():
    if  item[0] in 'aeiouAEIOU':
        vowelcount = vowelcount + item[1]
    elif not item[0].isspace():
        conscont = conscont + item[1]     
    print(item[0],item[1],sep='-')
print("number of vowels : ",vowelcount)
print("number of consonants : ",conscont) 

