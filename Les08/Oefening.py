invoeren = input('Geef een string op:')

for letter in invoeren:
    print('Uitkomst {} {} {:8b} {:x}'.format(letter, ord(letter),ord(letter),ord(letter)))





# print('De ASCII waarden is {}'.format(asc)) #ASC waarden, omdat die hierboven al gedaan is
# print('De ASCII waarden is {:b}'.format(asc)) # Bina waarden omdat we er :b inzetten
# print('De ASCII waarden is {:x}'.format(asc)) # Hexid. omdat we een :x invoeren
