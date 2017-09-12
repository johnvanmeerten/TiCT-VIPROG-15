invoer = input('Geef woord op: ')

teller1 = 0
teller2 = 0
teller3 = 0

for woord in invoer:
    if woord == 'e':
        teller1 = teller1 + 1
    elif woord == 'o':
        teller2 = teller2 + 1
    elif woord == 'i':
        teller3 = teller3+ 1

print('Het woord bevat ' +str(teller1) + ' keer letter e')
print('Het woord bevat ' +str(teller2) + ' keer letter o')
print('Het woord bevat ' +str(teller3) + ' keer letter i')