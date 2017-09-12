getallenrij = [23, 35, 31, 26, 73, 75, 84, 29, 42, 46]

Teller = 0

for getal in getallenrij:
    if getal % 2 == 1:
        Teller = Teller+1
print('Het aantal oneven getallen is '+(str(Teller)))


teller1 = 0

for getal in getallenrij:
    if getal % 2 == 0 and getal % 3 == 0:
        teller1 = teller1 + 1
print('Het aantal getallen deelbaar door en en 3 is '+str(teller1))