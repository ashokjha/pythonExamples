string = str(input("Enter a line : "))
lst = string.split( )
print(type(lst))
numofw = 0
for i in lst:
      sublst = i.split()
      if i[0] == "a" or i[0] == "e" or i[0] == "i" or i[0] == "o" or i[0] == "u":
            numofw += 1
print("No of word starting with vowel = ",numofw)
