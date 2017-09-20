import time

Naam = input('Geef naam: ')
tijd = time.strftime('%A %b/%d/%y %I:%M %p', time.localtime())


infile = open('Hardlopers.txt', 'r')
inhoud = infile.write()

#Hier nog afmaken qua outp string en het bestand sluiten