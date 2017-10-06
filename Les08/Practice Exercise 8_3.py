naam = input('Geef uw naam: ')
beginS = input('Geef begin station: ')
eindS = input('Geef eind station: ')


def code (invoerstring):
    nieuwestring = ''
    for char in invoerstring:
        nieuweASCII = ord(char)+3
        nieuwechar = chr(nieuweASCII)
        nieuwestring += nieuwechar
    return nieuwestring


gebcomstring = naam+beginS+eindS
uitvoerstring = code(gebcomstring)
print(uitvoerstring)