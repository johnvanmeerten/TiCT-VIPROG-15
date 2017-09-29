invoeren = eval(input('Hoe groot moet het zijn? '))

import random



def diceprob(invoersom):
    aantalworpen = 0
    aantalworpen_ingevoerd = 0
    while aantalworpen_ingevoerd < 100:
        worp1 = random.randrange(1, 7)
        worp2 = random.randrange(1, 7)
        som = worp1+worp2
        if som == invoersom:
            aantalworpen_ingevoerd += 1
        aantalworpen += 1

    print('Het aantal benodige worpen is {}'.format(aantalworpen))




diceprob(invoeren)
















