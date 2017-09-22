invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

getallen = list(map(int, invoer.split('-')))

getallen.sort()

print('Gesorteerde list van ints: {}'.format(getallen))
print('Grootste getal: {} en Kleinste getal: {}'.format(max(getallen), min(getallen)))
print('Aantal getallen: {} en som van de getallen {}'.format(len(getallen), sum(getallen)))
print('Gemiddelde: {}'.format(sum(getallen)/len(getallen)))