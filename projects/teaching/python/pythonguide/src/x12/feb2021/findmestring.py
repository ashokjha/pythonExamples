linestr = input()
substr = input()
cnt = 0
substr_len = len(substr)
while substr in linestr:
    cnt += 1 
    linestr = linestr[(linestr.find(substr) + substr_len):]        
print(cnt)
