def sortlexically(ln):
    wrdlst=ln.split()
    for pos in range(1, len(wrdlst)):
        key = wrdlst[pos]
        j = pos - 1  
        while j >= 0 and key < wrdlst[j]:
            wrdlst[j + 1] = wrdlst[j]
            j = j - 1
        wrdlst[j + 1] = key
    return wrdlst
print("Input")
inpdata = input(" ")
print("Output")
for s in sortlexically(inpdata):
    print(s)


