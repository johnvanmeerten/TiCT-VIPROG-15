woorden = eval(input("Geef lijst met minimaal 10 strings: "))

tijdelijk = []

for woord in woorden:
    if len(woord) <= 4:
        tijdelijk.append(woord)
print(tijdelijk)