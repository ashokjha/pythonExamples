'''
7. Write a program to accept a sentence and perform the following tasks:
(a) Arrange the words contained in the sentence according to the size of
    the words in ascending order. If two words are of the same length then
    the first occurring comes first. [5]
(b) Count number of words starting with vowel.
Example:
INPUT: A STITCH IN TIME SAVES NINE
OUTPUT:
AFTER ARRANGING: A IN TIME NINE SAVES STITCH
NO OF WORDS: 02


def startwithVowel(w):
    return w[0] in 'AEIOUaeiou'

line = input("INPUT: ")
wordsl = (line.strip()).split()
wordsl.sort(key=len)
print("Output:")
print(" ".join(wordsl))
numoword = sum(startwithVowel(word) for word in wordsl) 
print("NO OF WORDS:",numoword)
'''

def mystery(s):
    i = 0
    result = ''

    while not s[i].isdigit():
          result = result + s[i]
          i = i + 1

    return result

def example(L):
    """ (list) -> list
    """
    i = 0
    result = []
    while i < len(L):
        result.append(L[i])
        i = i + 3
    return result

def compress_list(L):
    """ (list of str) -> list of str

    Return a new list with adjacent pairs of string elements       from Lconcatenated together, starting with indices 0 and 1,    2 and 3,and so on.

    Precondition: len(L) >= 2 and len(L) % 2 == 0

    >>> compress_list(['a', 'b', 'c', 'd'])
    ['ab', 'cd']
    """ 
    compressed_list = []
    i = 0

    while i < len(L):
        compressed_list.append(L[i] + L[i + 1])
        i=i+2

    return compressed_list

def sumeven() :
      s=0
      for t in range (524,10508+1,2):
          s=s+t
      n = int((10508-524)/2)+1
      print(n)
      return s

          
def while_version(L):
    """ (list of number) -> number
    """
    i = 0
    total = 0

    while i < len(L) and L[i] % 2 != 0:
        total = total + L[i]
        i = i + 1

    return total    
    
def for_version1(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0 and not found_even:
            total = total + num
        else:
            found_even = True
 
    return total

    
def for_version2(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0:
            total = total + num
        found_even = True

    return total    
    
def for_version3(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0:
            total = total + num
        elif not found_even:
            found_even = True

    return total    
    
def for_version4(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0:
            total = total + num
            found_even = True

    return total


def increment_items(L, increment):
    i = 0
    while i < len(L):
        L[i] = L[i] + increment
        i = i + 1

values = [1, 2, 3]
#print(increment_items(values, 2))
#print(values)

values = []
for num in range(1, 4):
    values.append(num * 3)
print(values)


for num in range(3, 19, 8):
    print(num)
