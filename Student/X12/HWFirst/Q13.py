x=5
def func2():
    global x
    x=x+1
    print (x)
x=7
func2()
print(x)