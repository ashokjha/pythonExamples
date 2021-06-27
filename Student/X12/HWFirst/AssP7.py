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

'''
def sortwordasc(line):
    wordsl = (line.strip()).split()
    wordsl.sort(key=len)
    return " ".join(wordsl)

def startwithVowel(w):
    return w[0] in 'AEIOUaeiou'

def numofwordstwiVowel(line):
    numofw = 0
    for w in line.split():
        if startwithVowel(w):
            numofw = numofw +1
    return numofw

if __name__ == '__main__':
    line = input("INPUT: ")
    print(sortwordasc(line))
    print("NO OF WORDS:{:02d}".format(numofwordstwiVowel(line)))