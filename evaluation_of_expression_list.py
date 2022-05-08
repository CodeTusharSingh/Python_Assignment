print("Don't use parentheses in this program")
x = str(input("Enter the arthmetic equation: "))
a = list(x)
b = []
op1 = ''
for i in range(0, len(a)):
    op2 = ''
    if(ord(a[i]) >= 48 and ord(a[i]) <= 57):
        op1 += a[i]
    if(a[i] == '+' or a[i] == '-' or a[i] == '/' or a[i] == '*' or a[i] == '^' or a[i] == '(' or a[i] == ')'):
        op2 += a[i]
        if(op1 == ''):
            b.append(op2)
        else:
            b.append(op1)
            op1 = ''
            b.append(op2)
b.append(op1)
if(a[len(a)-1] == ')'):
    b.remove('')
print(b)
print("``````Evaluation``````")
c1 = 0
for i in range(0, len(b)):
    if(b[i] == '+' or b[i] == '-'):
        c1 += 1
c2 = 0
for i in range(0, len(b)):
    if(b[i] == '+' or b[i] == '-'):
        b[i:i+2] = [''.join(b[i:i+2])]
        c2 += 1
    if(c1 == c2):
        break
print(b)
for i in range(0, len(b)):
    if(b[i] == '/' or b[i] == '*' or b[i] == '^' or b[i] == '(' or b[i] == ')'):
        continue
    else:
        b[i] = int(b[i])
print(b)
r = 0
i = 0
while(i < len(b)):
    if(b[i] == '^'):
        r1 = b[i-1] ** b[i+1]
        b.remove(b[i+1])
        b.insert(i+1, r1)
        b.remove(b[i])
        b.remove(b[i-1])
        i = 0
    i += 1
i = 0
while(i < len(b)):
    if(b[i] == '/'):
        r1 = b[i-1] / b[i+1]
        b.remove(b[i+1])
        b.insert(i+1, r1)
        b.remove(b[i])
        b.remove(b[i-1])
        i = 0
    i += 1
i = 0
while (i < len(b)):
    if(b[i] == '*'):
        r2 = b[i-1] * b[i+1]
        b.remove(b[i+1])
        b.insert(i+1, r2)
        b.remove(b[i])
        b.remove(b[i-1])
        i = 0
    i += 1
for i in range(0, len(b)):
    r += b[i]
print(x, "=", r)

# A CODE BY TUSHAR SINGH