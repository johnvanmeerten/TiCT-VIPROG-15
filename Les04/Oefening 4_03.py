lst = [4, 0, 1, -2]

def swap (x):
    if len(x) >1:
        x[0], x[1] = x[1], x[0]

print(lst)
swap(lst)
print(lst)
