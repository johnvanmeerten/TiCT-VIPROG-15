infile = open('Voorbeeld5_5.txt', 'r')
inhoudt1 = infile.read()
infile.close()
inhoud2 = inhoudt1.split()
print(inhoud2)