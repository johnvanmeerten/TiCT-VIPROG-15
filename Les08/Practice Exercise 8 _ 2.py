import random

def monopolyworp():
    count = 0

        while True:
            count += 1
            worp1 = random.randrange(1, 7)
            worp2 = random.randrange(1, 7)
            if worp1 == worp2:
                print(worp1 + worp2)