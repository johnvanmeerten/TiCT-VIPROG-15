infile = open('kaartnummers.txt', 'r')
regels = infile.readlines()
infile.close()

outfile = open('kaartnummersuit.txt', 'w')

for regel in regels:
    kaartinfo = regel.split(',')
    outfile.write(kaartinfo[1].strip() + ' heeft kaartnummer: ' + kaartinfo[0] + '\n')

outfile.close()