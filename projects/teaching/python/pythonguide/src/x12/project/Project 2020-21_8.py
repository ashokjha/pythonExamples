#[19,2,31,45,30,11,121,27]
l = eval(input("Input list of numbers: "))
for idx in range(len(l)):
      min_idx = idx
      for j in range( idx +1, len(l)):
            if l[min_idx] > l[j]:
                  min_idx = j
            l[idx], l[min_idx] = l[min_idx], l[idx]
print(l)
