n=int(input())
lst=[]

for i in range(n):
      tname=input()
      score=int(input())
      lst.append([tname,score])
print(lst)
for i in range(len(lst)):
      m= i
      for j in range(i+1, len(lst)):
            if lst[m][1] > lst[j][1]:
                  m = j
      lst[i], lst[m] = lst[m], lst[i]
print(lst)
print(lst[-1][0])
print(lst[0][0])


