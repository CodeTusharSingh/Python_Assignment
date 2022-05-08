from statistics import mode
import time
start = time.time()
print(start)
x = list(map(int, input("Enter multiples values: ").split()))
print("List of numbers you entered is:", x)
if(len(x) == 1):
    print("HCF of", x, "=", x[0])
    end = time.time()
    print(end-start)
    exit()
a = []
s = 1
k = 0
for i in range(0, len(x)):
    c = 0
    for j in range(1, x[i]+1):
        if(x[i] % j == 0):
            c += 1
    if(c == 2):
        k += 1
if(k == len(x)):
    print("HCF of", x, "=", 1)
    end = time.time()
    print(end-start)
    exit()
for i in range(0, len(x)):
    j = 1
    while(j != x[i]+1):
        if(x[i] % j == 0):
            a.append(j)
        j = j+1
b = []
for i in range(0, len(a)):
    for j in range(0, i):
        if(a[i] == a[j]):
            b.append(a[i])
print(a)
print(b)
z = []
for i in range(0, len(b)):
    for j in range(0, i):
        if(b[i] == b[j]):
            z.append(b[i])
print(z)
print("HCF of", x, "=", max(z))
end = time.time()
print(end-start)

# A CODE BY TUSHAR SINGH