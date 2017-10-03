bedrag = eval(input('Wat is het bedrag? '))
rentepercentage = eval(input('Wat is het rentepercentage? '))

def eindbedrag(bedrag, rentepercentage):
    nieuwbedrag = bedrag+rentepercentage*bedrag/100
    return (nieuwbedrag)

resultaat = eindbedrag(bedrag, rentepercentage)

print(resultaat)