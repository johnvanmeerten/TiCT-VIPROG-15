def berekensomevengetallen (getallenrij):
    som = 0
    for getal in getallenrij:
        if getal %2 == 0:
            som += getal
    return (som)

def berekensomonevengetallen (getallenrij):
    som = 0
    for getal in getallenrij:
        if getal %2 == 1:
            som += getal
    return (som)



getallenrij = [23, 35, 31, 26, 73, 75, 84, 29, 42, 46]

print('De som van de even getalen bedraagdt {}'.format(berekensomevengetallen(getallenrij)))
print('De som van de onevengetallen bedraagt {}'.format(berekensomonevengetallen(getallenrij)))