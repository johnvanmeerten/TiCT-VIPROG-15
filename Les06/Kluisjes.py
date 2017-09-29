print('1: Ik wil weten hoeveel kluizen er nog vrij zijn')
print('2: Ik wil een nieuwe kluis')
print('3: Ik wil even iets uit mijn kluis halen')


invoer = eval(input('Wat is uw keuze? '))

if invoer >= 4:
    print('Dit is een onjuiste keuze, kies opnieuw')

def toon_aantal_kluizen_vrij():
    filenaam = open('kluisjes.txt', 'r')
    regels = filenaam.readlines()
    filenaam.close()
    print(12 - len(regels))

