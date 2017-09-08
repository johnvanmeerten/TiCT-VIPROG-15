lst = [1, 4, 6, 3, 2, 4, 7]
index = (int(len(lst)/2))
print(index)

print(lst[index])

lst.sort(reverse=True)
print(lst)

x = lst[0]
lst.pop(0)
lst.append(x)

print(lst)