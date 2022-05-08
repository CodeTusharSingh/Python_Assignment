a = []
b = []


class contact:
    def __init__(self, name, number,):
        self.name = name
        self.number = number

    def write_contact(self):
        f1 = open("phonebook.txt", "a")
        f1.write(self.name)
        f1.write("\n")
        f1.write(self.number)
        f1.write("\n")
        f1.close()

    def read_contact(self):
        f2 = open("phonebook.txt", "r")
        self.name = f2.read()
        print(self.name)
        f2.close()


n = int(input("How many inputs you want to insert inside the file: "))
i = 0
while(i < n):
    name = str(input("Enter the name of contact: "))
    number = str(input("Enter the phone number of the person: "))
    cont = contact(name, number)
    write = cont.write_contact()
    i += 1
read = cont.read_contact()
f = open("phonebook.txt", "r")
ap = f.readlines()
f.close()
print(ap)
nw1 = []
nw2 = []
for i in range(len(ap)):
    nw1.append(ap[i])
    nw1 = "".join(nw1)
    nw1 = list(nw1)
    nw1.remove('\n')
    j = 0
    while (j < len(nw1)):
        if(len(nw1[j]) == 1):
            nw1[j: len(nw1)] = ["".join(nw1[j: len(nw1)])]
            nw2.append(nw1[j])
        j += 1
    nw1 = []
print(nw2)
for i in range(len(nw2)):
    if(i % 2 == 0):
        a.append(nw2[i])
    else:
        b.append(nw2[i])
print(a)
print(b)

f = open("phonebooklist.txt", "w")
m1 = []
for i in range(0, len(a)):
    m1.append(len(a[i]))
x1 = max(m1)
m2 = []
for i in range(0, len(b)):
    m2.append(len(b[i]))
x2 = max(m2)
print('-'*(x1+x2+4+15))
f.write('-'*(x1+x2+4+15)+"\n")
print("| SN | Name | Phone No. |")
f.write("| SN | Name | Phone No. |"+"\n")
print('-'*(x1+x2+4+15))
f.write('-'*(x1+x2+4+15)+"\n")
for i in range(0, len(a)):
    i1 = str(i+1)
    print("|", i1, ' '*(3-len(i1)), "|", a[i], ' '*(
        (x1) - len(a[i])), "|", b[i], ' '*((x2) - len(b[i])), "|")
    f.write("| " + i1 + ' '*(3-len(i1)) + " | " + a[i] + ' '*(
        (x1) - len(a[i])) + " | " + b[i] + ' '*((x2) - len(b[i])) + " |"+"\n")
    print('-'*(x1+x2+4+15))
    f.write('-'*(x1+x2+4+15)+"\n")
f.close()

# A CODE BY TUSHAR SINGH