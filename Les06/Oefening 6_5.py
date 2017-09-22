tabel = [[4, 7, 2, 5], [5, 2, 9, 2, 4, 3, 4], [8, 3, 6, 6]]

for rij in range(len(tabel)):
    for kolom in range(len(tabel[rij])):
        print(tabel[rij][kolom], end = ' ')
    print()