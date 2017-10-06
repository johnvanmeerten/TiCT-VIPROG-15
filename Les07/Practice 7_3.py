dict = {'Tim':8.2, 'Bob':7.2, 'Sanne':9.4, 'Ana':9.4, 'John':9.8, 'Pim':4.2, 'Elvira':7.2, 'Ramona':8.2}

for naam, cijfer in dict.items():
    if cijfer > 9:
        print(naam, cijfer)

print(dict['Tim'])