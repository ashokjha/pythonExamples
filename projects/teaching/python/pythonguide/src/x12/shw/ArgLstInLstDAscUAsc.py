
def insertionSort(data):
    for pos in range(1, len(data)):
        key = data[pos]
        j = pos - 1  
        while j >= 0 and (key%10) < (data[j]%10):
            data[j + 1] = data[j]
            j = j - 1
        data[j + 1] = key

if __name__ == '__main__':
    print("Input")
    N = int(input(""))
    lst=[]
    for i in range(N):
        lst.append(int(input("")))
    
    insertionSort(lst)
    print('Output')
    for i in lst:
        print(i,end=' ')


