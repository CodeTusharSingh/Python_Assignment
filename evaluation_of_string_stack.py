s = []
tos = -1


def push(a):
    global tos
    tos += 1
    s.insert(tos, a)
    return s


def pop():
    global tos
    p = ''
    if (tos <= -1):
        (print("Stack is empty!!!"))
        return -1
    else:
        p = s.pop(tos)
        tos -= 1
        return p


def top():
    t = ''
    t = s[len(s)-1]
    return t


def empty():
    return (tos <= -1)



precedence = {
    '/': 3,
    '*': 3,
    '+': 2,
    '-': 2,
    '(': -1,
    ')': -1,
}

x = str(input("Enter the arthmetic equation: "))
st = ''
for i in range(0, len(x)):
    if(x[i] != '*' and x[i] != '/' and x[i] != '-' and x[i] != '+' and x[i] != '(' and x[i] != ')'):
        st += x[i]
    elif(x[i] == '('):
        push(x[i])
    elif(x[i] == ')'):
        while(empty() == False and top() != '('):
            st += top()
            pop()
        if(empty() == False):
            pop()
    else:
        while(empty() == False and precedence[top()] >= precedence[x[i]]):
            st += top()
            pop()
        push(x[i])
while(empty() == False):
    st += top()
    pop()
print("Postfix expression:", st)
st = list(st)
ch = ''
ex = []
for i in range(0, len(x)):
    if(x[i] != '*' and x[i] != '/' and x[i] != '-' and x[i] != '+' and x[i] != '(' and x[i] != ')'):
        ch += x[i]
        ex.append('#')
    elif(x[i] == '*' or x[i] == '/' or x[i] == '-' or x[i] == '+' or x[i] == '(' or x[i] == ')'):
        ex.append(ch)
        ch = ''
ex.append(ch)
k = 0
while k < len(ex):
    if(ex[k] == ''):
        ex.pop(k)
    k += 1
for i in range(0,len(st)):
    if(st[i] != '*' and st[i] != '/' and st[i] != '-' and st[i] != '+'):
        limit = i
for i in range(limit+1,len(st)):
    ex.append(st[i])
for i in range(0, limit+1):
    if(st[i] == '*' or st[i] == '/' or st[i] == '-' or st[i] == '+'):
        if(ex[i+3] != '#'):
            ex.insert(i+3, '#')
            ex.pop(i+3)
            ex.insert(i+3, st[i])
        else:
            ex.pop(i+3)
            ex.insert(i+3, st[i])
k = 0
while k < len(ex):
    if(ex[k] == '#'):
        ex.remove('#')
        k=0
    k += 1
r = ''
for i in range(0, len(ex)):
    if(ex[i] != '*' and ex[i] != '/' and ex[i] != '-' and ex[i] != '+'):
        push(ex[i])
    else:
        s1 = top()
        pop()
        s2 = top()
        pop()
        if(ex[i] == '+'):
            r = float(s2) + float(s1)
        elif(ex[i] == '-'):
            r = float(s2) - float(s1)
        elif(ex[i] == '/'):
            r = float(s2) / float(s1)
        elif(ex[i] == '*'):
            r = float(s2) * float(s1)
        push(r)
inf = top()
print(x,"=", inf)

# A CODE BY TUSHAR SINGH