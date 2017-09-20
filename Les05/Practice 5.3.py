infile = open('kaartnummers.txt', 'r')
inhoud = infile.readlines()
infile.close()

hoogste = 0

for regel in inhoud:
    kaartinfo = regel.split(',')


    nr = int(kaartinfo[0].strip())
    print(type(nr))
    # if kaartinfo[0].strip() > hoogste:
    #     hoogste = kaartinfo[0].strip()
print(hoogste)
