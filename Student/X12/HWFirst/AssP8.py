'''
8. Write a program to input a sentence from user and perform the following operation:
(i) Count the number of palindrome words.
(ii) Display the longest word/s of the sentence.

Example:
Sample Input: I love my mom and dad. 
Sample Output: 
Count of Palindrome words: 2
Longest word: love
'''
def ispalindrome(w):
    return w==w[-1::-1]

line = input("Sample Input: ")
wordsl = (line.strip()).split()
print("Sample Output:")
wordsl.sort(key=len,reverse=True)
print("AFTER ARRANGING:"," ".join(wordsl))
numoword = sum(ispalindrome(word) for word in wordsl) 
print("Count of Palindrome words:",numoword)
print("Longest word:",wordsl[0])

