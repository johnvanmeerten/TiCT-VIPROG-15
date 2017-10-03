import random

def monopolyworp():
    count = 0
    while True:
        count += 1
        worp1 = random.randrange(1, 7)
        worp2 = random.randrange(1, 7)
        if worp1 == worp2:
            # gelijk
            if count > 2:
                print('{} + {} = (direct naar gevangenis)'.format(worp1, worp2))
            else:
                print('{} + {} = {:2} (dubbel)'.format(worp1, worp2, (worp1 + worp2)))
        else:
            # ongelijk
            print('{} + {} = {}'.format(worp1, worp2, (worp1+worp2)))


            break

for x in range(200):
    monopolyworp()