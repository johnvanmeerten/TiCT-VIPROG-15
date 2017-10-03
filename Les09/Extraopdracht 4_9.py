
def voegnaamtoe():
    namen = []
    while True:
        invoer = input('Geef namen op: ')
        if invoer == '':
            break
        namen.append(invoer)
    return namen

print(voegnaamtoe())

