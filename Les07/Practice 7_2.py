

while True:
    invoer = input('Geef een string van vier letters: ')
    if len(invoer) == 4:
        print('Inlezen van correcte string: {} is geslaagd'.format(invoer))
        break
    else:
        print('{} heeft {} letters'.format(invoer, len(invoer)))