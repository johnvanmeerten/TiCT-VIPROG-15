import csv

with open('magazijn.csv', 'w', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    writer.writerow(('Artikelnummer','Artikellcode','Naam','Voorraad','Prijs'))
    while True:
        artikelnummer = input('Wat is het Artikelnummer?')
        if artikelnummer == 'eind':
            break
        artikelcode = input('Wat is het Artikelcode?')
        naam = input('Wat is de naam?')
        voorraad = input('Wat is de voorraad?')
        prijs = input('Wat is de prijs?')
        writer.writerow((artikelnummer, artikelcode, naam, voorraad, prijs ))