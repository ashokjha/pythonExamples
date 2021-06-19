linestr = input()
vowellist='A E I O U'.split()
cnt = 0
for wrd in linestr.split():
      wrd=wrd.strip()
      if(wrd[0] in vowellist and wrd[-1] in vowellist ):
            cnt +=1
print(cnt)
