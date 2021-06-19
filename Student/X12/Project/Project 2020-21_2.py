
inpt = "geeks for geeks@121$"
inpt = input("Input a string : ")
vowels = 0
consonant = 0
specialChar = 0
digit = 0
for i in range(0, len(inpt)):
      ch = inpt[i]
      if ( (ch >= 'a' and ch <= 'z') or   (ch >= 'A' and ch <= 'Z') ): 
            ch = ch.lower() 
            if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'): 
                  vowels += 1
            else: 
                  consonant += 1
      elif (ch >= '0' and ch <= '9'): 
            digit += 1
      else: 
            specialChar += 1
print("Vowels:", vowels) 
print("Consonant:", consonant) 
print("Digit:", digit) 
print("Special Character:", specialChar) 


