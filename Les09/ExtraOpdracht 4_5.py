def berekensomevengetallen (getallenrij):
    tijdelijk = 0
    for getal in getallenrij:
        if getal %2 == 0:
            tijdelijk += getal
    print(tijdelijk)


getallenrij = [23, 35, 31, 26, 73, 75, 84, 29, 42, 46]

berekensomevengetallen(getallenrij)
