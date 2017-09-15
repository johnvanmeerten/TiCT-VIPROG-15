lst = ('Eleanor', 'Evelyn', 'Sammy', 'Owen', 'Gavin')

def partition (x):
    TMPlst = []
    for naam in x:
        if naam[0] in 'ABCDEFGHIJKLM':
            TMPlst.append(naam)
    return TMPlst

print(partition(lst))
