'''
9. Write a program to accept a sentence and perform the following tasks:
(a) Arrange the words contained in the sentence according to the size of
    the words in ascending order. If two words are of the same length then
    the first occurring comes first. [5]
(b) Count number of words starting with vowel.

Example:
INPUT: A STITCH IN TIME SAVES NINE
OUTPUT:
AFTER ARRANGING: A IN TIME NINE SAVES STITCH
NO OF WORDS: 02
'''

def startwithVowel(w):
    return w[0] in 'AEIOUaeiou'

line = input("INPUT: ")
wordsl = (line.strip()).split()
wordsl.sort(key=len)
print("Output:")
print(" ".join(wordsl))
numoword = sum(startwithVowel(word) for word in wordsl) 
print("NO OF WORDS:",numoword)


