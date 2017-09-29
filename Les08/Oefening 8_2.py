set1 = set()
set2 = set()
set3 = set()
set4 = set()


for getal in range(0,1000):
    if getal % 3 == 0:
        set1.add(getal)
    if getal % 7 == 0:
        set2.add(getal)
    if getal % 3 == 0 and getal % 7 == False:
        set3.add(getal)
    if getal % 3 != 1 and getal % 7 != 0:
        set4.add(getal)

print(set1)
print(set2)
print(set3)
print(set4)