def toon_aantal_kluizen_vrij():
    infile = open('kluisjes.txt', 'r')
    kluizendata = infile.readlines()
    infile.close()
    aantalkluizen = len(kluizendata)
    aantalvrij = 12 - aantalkluizen
    print(aantalvrij)


def nieuwe_kluis():
    infile = open('kluisjes.txt', 'r')
    kluizendata = infile.readlines()
    infile.close()


def kluis_openen():
    infile = open('kluisjes.txt', 'r')
    kluizendata = infile.readlines()
    infile.close()
    stringnummer = input('Wat is je nummer? ')
    code = input('Wat is je code? ')
    gegevenscorrect = False
    for kluis in kluizendata:
        gegevensvan1kluis = kluis.split(';')
        stringnummer = gegevensvan1kluis[0]
        kluiscode = gegevensvan1kluis[1].strip()
        if stringnummer == stringnummer and code == kluiscode:
            gegevenscorrect = True
    if gegevenscorrect:
        print('Kluis wordt geopenend ')
    else:
        print('De kluis wordt niet geopend')


print('1: Ik wil weten hoeveel kluizen er nog vrij zijn')
print('2: Ik wil een nieuwe kluis')
print('3: Ik wil even iets uit mijn kluis halen')


keuze = eval(input('Wat is uw keuze? '))

if keuze == 1:
    toon_aantal_kluizen_vrij()
elif keuze == 2:
    nieuwe_kluis()
else:
    kluis_openen()



# def toon_aantal_kluizen_vrij():
#     filenaam = open('kluisjes.txt', 'r')
#     regels = filenaam.readlines()
#     filenaam.close()
#     print(12 - len(regels))

