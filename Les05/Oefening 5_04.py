leeftijd1 = 17
leeftijd2 = 18

som = leeftijd2 + leeftijd2

print('De som van de leeftijden is {}' .format(som))

weekdag = 'dinsdag'
dag = '25'
maand = 'maart'
uur = 14
minuten = 15

print('{} {} {}'.format(weekdag, dag, maand))
print('{} {} {} om {}.{} uur'.format(weekdag, dag, maand, uur, minuten))

for i in range(1, 8):
    print('{} {:2} {:3}'. format (i, i**2, 2**i))
