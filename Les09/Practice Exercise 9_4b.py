import csv

with open('magazijn.csv', 'r') as myCSVfile:
    reader = csv.DictReader(myCSVfile, delimiter = ';')
    maxprijs = 0
    for row in reader:
        prijs = float(row['Prijs'])
        if prijs > maxprijs:
            mapprijs = prijs
            maxnaam = row['Naam']
    print('Het duurste artikel is {} en die kost {} euro'.format(maxnaam, maxprijs))