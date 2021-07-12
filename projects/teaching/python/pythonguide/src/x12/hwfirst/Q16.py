
def insertionSort(data):

    for pos in range(1, len(data)):
        key = data[pos]
        j = pos - 1
        
        while j >= 0 and (key%10) < (data[j]%10):
            data[j + 1] = data[j]
            j = j - 1
        data[j + 1] = key


ll1 = eval(input(" "))
insertionSort(ll1)
print('Sorted List in Ascending Order:')
print(ll1)