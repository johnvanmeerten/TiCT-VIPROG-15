invoer = eval(input('Geef een getal: '))

getallen = []

while invoer != 0:
    print(invoer)
    getallen.append(invoer)
    invoer = eval(input('Geef een getal: '))
print('Er zijn {} getallen ingevoerd, de som is: {}'.format(len(getallen), sum(getallen)))