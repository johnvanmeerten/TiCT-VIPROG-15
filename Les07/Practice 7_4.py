def ticker(filename):
    file = open(filename, 'r')
    bedrijven = file.readlines()
    newdect = {}

    for bedrijf in bedrijven:
        dataregel = bedrijf.split(':')
        sleutel = dataregel[0]
        waarden = dataregel[1].strip()
        newdect[sleutel] = waarden
    return newdect


tickerbestand = ticker('Beurs.txt')


bedrijfsnaam = input('Geef naam van bedrijf: ')

for bedrijf in tickerbestand:
    if bedrijfsnaam == bedrijf:
        print(tickerbestand[bedrijf])