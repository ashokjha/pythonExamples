##message = 'Happy 29th!'
##new_message = ''
##
##for char in message:
##    if not char.isdigit():
##        new_message = new_message + char
##    else:
##        new_message = new_message + str((int(char) + 1) % 10)
##
##print(new_message)
##
def f(s):
    for char in s:
        if not (char in 'aeiouAEIOU'):
             print('b'+char+'b')

def w(s):
    i = 0
    while i < len(s) and not (s[i] in 'aeiouAEIOU'):
        print('wb'+s[i]+'b')
        i = i + 1
