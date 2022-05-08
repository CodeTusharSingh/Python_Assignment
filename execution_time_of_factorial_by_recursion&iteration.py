from time import time


f = open("factorial_file.txt", "w")
a = []
b = []
c = []
# ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Factorial by recursion~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

for i in range(5, 996):
    c.append(str(i))
    start1 = time()

    def fact(n):
        if(n > 0):
            return n*fact(n-1)
        elif(n == 0):
            return 1

    fact_val = fact(i)
    end1 = time()
    toe1 = end1 - start1
    a.append(str(toe1))

# ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Factorial by iteration~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for j in range(5, 996):
    start2 = time()
    i = 1
    s = 1
    while(i < j):
        i = i + 1
        s = s * i
    end2 = time()
    toe2 = end2 - start2
    b.append(str(toe2))
m1 = []
for i in range(0, len(a)):
    m1.append(len(a[i]))
x1 = max(m1)
m2 = []
for i in range(0, len(b)):
    m2.append(len(b[i]))
x2 = max(m2)
print('-'*(x1+x2+4+4+15))
f.write('-'*(x1+x2+4+4+15)+"\n")
print("| SN | Input | Time of execution by recursion | Time of execution by iteration |")
f.write("| SN | Input | Time of execution by recursion | Time of execution by iteration |"+"\n")
print('-'*(x1+x2+4+4+15))
f.write('-'*(x1+x2+4+4+15)+"\n")
for i in range(0, len(c)):
    i1 = str(i+1)
    print("|", i1, ' '*(3-len(i1)), "|", c[i], ' '*(3-len(c[i])), "|", a[i], ' '*(
        (x1) - len(a[i])), "|", b[i], ' '*((x2) - len(b[i])), "|")
    f.write("| " + i1 + ' '*(3-len(i1)) + " | " + c[i] + ' '*(3-len(c[i])) + " | " + a[i] + ' '*(
        (x1) - len(a[i])) + " | " + b[i] + ' '*((x2) - len(b[i])) + " |"+"\n")
    print('-'*(x1+x2+4+4+15))
    f.write('-'*(x1+x2+4+4+15)+"\n")
f.close()

# A CODE BY TUSHAR SINGH