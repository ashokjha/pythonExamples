import re
x= input("Please enter a stringh:")
x=x.replace(" ","")
pattern='[0-9]'
x = re.sub(pattern, '#', i) for i in x
print(x)