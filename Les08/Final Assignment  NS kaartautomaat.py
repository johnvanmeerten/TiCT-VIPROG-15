stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal',  'Amsterdam Amstel',  'Utrecht Centraal',  '’s-Hertogenbosch',   'Eindhoven',   'Weert', 'Roermond', 'Sittard', 'Maastricht']

def inlezen_beginstation(stations):
    beginstation = input('Geef begin station: ')
    while beginstation not in stations:
        beginstation = input('Niet juist, geef begin station: ')
    return beginstation

def inlezen_eindstation(stations, beginstations):
    eindstation = input('Geef eind station: ')
    while eindstation not in stations:
        eindstation = input('Niet juist, geef eind station: ')
    while stations.index(eindstation) < stations.index(beginstations):
        eindstation = input('Niet juist, geef eind station: ')
    return eindstation

def omroepen_reis(stations, beginstatios, eindstations):
    nummerB = stations.index(beginstatios) +1
    nummerE = stations.index(eindstations) +1
    afstand = nummerE-nummerB
    print('Het beginstation {} is het {} station in het traject'.format(beginstatios, nummerB))
    print('Het eindstation {} is het {} in het traject'.format(eindstations, nummerE))
    print('De afstand bedraagt {} station(s)'.format(nummerE-nummerB))
    print('De prijs van het kaart je {} euro'.format(5*afstand))

    print(' ')

    print('Jij stapt de trein in: {}'.format(beginstatios))
    for index in range(nummerB, nummerE-1):
        print('- {}'.format(stations[index]))

    print('Jij stapt uit: {} '.format(eindstations))

beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)