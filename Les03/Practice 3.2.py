leeftijd = eval(input('Geef je leeftijd: '))
paspoort = eval(input('Nederlands paspoort: '))

ja = True
nee = False

if leeftijd > 17 and paspoort == ja:
    print('Gefeliciteerd, je mag stemmen!')