a = [1, 1, 1, 2, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in range(len(a)):
    for j in range(len(b)):
        if(b[j] == a[i]):
            c.append(a[i])
i = 0
while i < len(c):
    j = 0
    while j < i:
        if(c[i] == c[j]):
            c.pop(i)
            j = 0
            i = 0
        j+=1
    i+=1
print(c)