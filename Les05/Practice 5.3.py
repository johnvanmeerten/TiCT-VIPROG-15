infile = open('kaartnummers.txt', 'r')
inhoud = infile.readlines()
infile.close()

hoogste = 0
regelnr = 1

for regel in inhoud:
    kaartinfo = regel.split(',')
    nr = int(kaartinfo[0])
    if nr > hoogste:
        hoogste = nr
        hoogsteregelnummer = regelnr
    regelnr = regelnr + 1

print('Deze file telt ' + str(regelnr) + ' regels')
print('Het grootste kaartnummer is: ' + str(hoogste) + ' en dat staat op regel ' + str(hoogsteregelnummer))



print('Deze file telt {} regels'.format(regelnr))
print('Het grootste kaartnummer is: {} en dat staat op regel {}'.format(hoogste, hoogsteregelnummer))