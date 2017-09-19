def convert(c):
    f = c * 1.8 + 32
    return f

def table ():
    print('    F     C')
    for f in range(-30, 41, 10):
        print('{:6.1f} {:6.1f}'.format(convert(f), f))

table()


