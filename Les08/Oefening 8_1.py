set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set3 = {1, 2}

print(set1.union(set2))  #vult aan
print(set1 | set2)

print(set1.intersection(set2))   # alleen wat in beide zit
print(set1 & set2)

print(set1.difference(set2))  #wat wel in de ene voorkomt maar niet in de andere
print(set1 - set2)
print(set2 - set1)

print(set3.issubset(set1)) #Hij kijkt of set3 een deel is van set1
print(set3 < set1)

print(set3.issuperset(set1)) #Dit is dus andersom dan die hierboven
print(set3 > set1)