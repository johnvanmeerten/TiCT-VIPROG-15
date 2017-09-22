def seizoen (getal):
    if getal >= 3 and getal <= 5:
        return ('lente')
    elif getal >= 6 and getal <= 8:
        return ('zomer')
    elif getal >= 9 and getal <= 11:
        return ('herfst')
    else:
        return ('winter')


getal = eval(input('Geeft getal op: '))
print(seizoen(getal))