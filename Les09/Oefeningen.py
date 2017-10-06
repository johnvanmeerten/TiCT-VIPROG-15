# Waarom is het wat het is bij deze?

import random

worpen = set()

for i in range(0, 20):
    dice = random.randrange(1, 6)
    print(str(dice), end = '-')
    worpen.add(dice)
print()
print(worpen)

# Deze hieronder heeft een andere oplossing dan gegeven wordt in de formative toets, waarom is dat?

woorden = ['Hogeschool', 'Utrecht', 'Hogeschool', 'Utrecht', 'Python']
for woord in woorden:
    if woord == 'Utrecht':
        print(woord, end=' ')
    else:
        continue

    print('Hogeschool', end=' ')



