'''
10. Write a program to input a sentence from user and perform the following operation:
(i) Count the number of palindrome words.
(ii) Display the longest word/s of the sentence.

Example:
Sample Input: I love my mom and dad.
Sample Output:
Count of Palindrome words: 2
Longest word: love
'''
def ispalindrome(w):
    return w == w[-1::-1]

def numberOfpalindrome(line):
    wordsl=line.split()
    numoword = sum(ispalindrome(word) for word in wordsl) 
    return numoword

def firstlongestword(line):
    words=line.split()
    dct = {}
    for w in words:
        wl=len(w)
        ll=dct.get(wl,[])
        ll.append(w)
        dct[wl]= ll
    lst = list(dct.keys())
    lst.sort()      
    return dct[lst[-1]][0]if lst else ''

line = input("Input: ")


print("Sample Output:")

print("Count of Palindrome words:",numberOfpalindrome(line))

print("Longest word:",firstlongestword(line))


