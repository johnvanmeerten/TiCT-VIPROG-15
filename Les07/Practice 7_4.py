def ticker(filename):
    file = open(filename, 'r')
    bedrijven = file.readlines()
    newdect = {}

    for bedrijf in bedrijven:
        data = bedrijf.split(':')
        newdect[data[0]] = data[1]
    file.close()
    return newdect

def ticker1(newdect, input):
    for tick in newdect:
        if input == tick:
            print('Ticker Symbol: {}'.format(newdect[tick]))
        elif newdect[tick] == input:
            print('Company name: {}'.format(tick))


newdect = ticker('Beurs.txt')

invoer = input('Hallo: ')

ticker1(newdect, invoer)

