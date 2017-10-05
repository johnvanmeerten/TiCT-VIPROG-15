dict = {'aa': [50, 27], 'bb': [20, 109], 'cc': [18, 25], 'dd': [60, 163], 'ee': [27, 12], 'ff': [92, 105], 'gg': [46, 70], 'hh': [82, 14], 'ii': [30, 53], 'jj': [52, 17], 'kk': [40, 1], 'll': [54, 159], 'mm': [48, 148], 'nn': [12, 70], 'oo': [33, 87], 'pp': [54, 137], 'qq': [33, 137], 'rr': [84, 189], 'ss': [58, 85], 'tt': [85, 44]}

import math

def naam_leeftijd():
    namen_passagiers = []
    while True:
        naam_passagier = input('Wat is uw naam? ')
        if naam_passagier == '':
            break
        leeftijd_passagier = eval(input('Wat is uw leeftijf'))
        namen_passagiers.append([naam_passagier, leeftijd_passagier])
    return namen_passagiers

def breken_afstand(begin,eind):
    _begin = dict.get(begin)
    _eind = dict.get(eind)
    x = _begin[0]-_eind[0]
    y = _begin[1]-_eind[1]
    z = math.sqrt(x**2+y**2)
    return z

def prijs(leeftijd, afstand):
    _basisprijs = afstand*0.70
    if leeftijd <= 4:
        _basisprijs = _basisprijs*1.40
    elif leeftijd >= 65:
        _basisprijs = _basisprijs*0.80
    return _basisprijs

print(dict)
waarheen = input('Waar wilt u heen? ')
afkomst = input('Waar komt u vandaan? ')
passagiers = naam_leeftijd()

for passagier in passagiers:
    print('Uw naam is {} en u bent {} jaren oud. \n De kosten voor uw ticket zijn {:.2f}'.format(passagier[0], passagier[1], prijs(passagier[1],breken_afstand(afkomst, waarheen))))