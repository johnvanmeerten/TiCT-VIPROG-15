s = 'abcdefghijklmnopqrstuvwxyz'

if s[1:3] == 'bc':
    print('True')
if s[0:14] == 'abcdefghijklmn':
    print('True')
if s[14:] == 'opqrstuvwxyz':
    print('True')
if s[1:-3] == 'bcdefghijklmnopqrstuvw':
    print('True')

print(s[1:3])    #A
print(s[0:14])   #B
print(s[14:])    #C
print(s[1:-3])   #D