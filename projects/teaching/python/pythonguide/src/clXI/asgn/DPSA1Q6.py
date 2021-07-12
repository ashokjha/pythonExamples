for num in range(2, 10):
      if num % 2 == 0:
            print("Found an even number", num)
            continue
      print("Found a number", num)

num = 2
while num < 10:
      if num % 2 == 0:
            print("Found an even number", num)
            num +=1
            continue
      else:
            print("Found a number", num)
            num +=1


