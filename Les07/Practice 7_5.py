

dict1 = {}

while True:
    naam = input('Volgende naam: ')
    if naam == '':
        break
    else:
        if naam in dict1:
            dict1[naam] += 1
        else:
            dict1[naam] = 1
print(dict1)