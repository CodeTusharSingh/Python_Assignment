def infpost(j, k, b):
    i = 0
    if (j > k):
        while(i < len(b)):
            if(b[i] == '/'):
                r = b[i-1] + b[i+1]
                b.remove(b[i+1])
                b.insert(i+1, r + '/')
                b.remove(b[i])
                b.remove(b[i-1])
                i = 0
            if(b[i] == '*'):
                r = b[i-1] + b[i+1]
                b.remove(b[i+1])
                b.insert(i+1, r + '*')
                b.remove(b[i])
                b.remove(b[i-1])
                i = 0
            i += 1
        i = 0
    elif (j < k):
        while(i < len(b)):
            if(b[i] == '*'):
                r = b[i-1] + b[i+1]
                b.remove(b[i+1])
                b.insert(i+1, r + '*')
                b.remove(b[i])
                b.remove(b[i-1])
                i = 0
            if(b[i] == '/'):
                r = b[i-1] + b[i+1]
                b.remove(b[i+1])
                b.insert(i+1, r + '/')
                b.remove(b[i])
                b.remove(b[i-1])
                i = 0
            i += 1
        i = 0

    while(i < len(b)):
        if(b[i] == '+'):
            r = b[i-1] + b[i+1]
            b.remove(b[i+1])
            b.insert(i+1, r + '+')
            b.remove(b[i])
            b.remove(b[i-1])
            i = 0
        if(b[i] == '-'):
            r = b[i-1] + b[i+1]
            b.remove(b[i+1])
            b.insert(i+1, r + '-')
            b.remove(b[i])
            b.remove(b[i-1])
            i = 0
        i += 1


print("``````Infix to Postfix``````")
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
c = []
for i in range(0, len(b)):
    c.append(b[i])
flag1 = 0
for y in range(0, len(b)):
    if (b[y] == ')'):
        flag1 += 1
flag2 = 0
for t in range(0, len(b)):
    if (b[t] == ')'):
        u = t
        for x in range(0, len(b)):
            if (b[x] == '('):
                d = []
                l = x
                f1 = t - l
                while(l <= t):
                    d.append(b[l])
                    l += 1
                jp = 0
                while(jp < len(d)):
                    if(d[jp] == '*'):
                        break
                    jp += 1
                kp = 0
                while (kp < len(d)):
                    if(d[kp] == '/'):
                        break
                    kp += 1
                infpost(jp, kp, d)
                d.remove('(')
                d.remove(')')
                print(d)
                d = ''.join(d)
                f2 = 0
                while(x <= t):
                    b.pop(x)
                    f2 += 1
                    if(f2 == f1+1):
                        break
                b.insert(x, d)
                x = 0
                break
        t = 0
        flag2 += 1
        if(flag1 == flag2):
            break


j = 0
while(j < len(c)):
    if(c[j] == '*'):
        break
    j += 1
k = 0
while (k < len(c)):
    if(c[k] == '/'):
        break
    k += 1
infpost(j, k, b)
print(b)
s = ''.join(b)
print("Postfix expression:", s)

# A CODE BY TUSHAR SINGH