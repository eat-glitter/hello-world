a = [4, 6, 5, 2, 7, 6, 3, 3, 9, 5, 0, 1, 2]

i = 0
b = []

while i < (len(a)):
    if a[i] not in b:
        b.append(a[i])
    i+=1

print(a)
print(b)
