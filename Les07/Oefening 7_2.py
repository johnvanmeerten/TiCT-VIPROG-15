week = {'ma': 'maandag', 'di': 'dindag', 'wo': 'woensdag', 'do': 'donderdag', 'vr': 'vrijdag' }

for afkoring in week.keys():
    print(afkoring)

for langenaam in week.values():
    print(langenaam)

for beide in week.items():
    print(beide)

for afkoring in week.keys():
    print(afkoring, week[afkoring])

for afkoring in week:
    print('Afkorting: {}, lange naam: {}'.format(afkoring, week[afkoring]))