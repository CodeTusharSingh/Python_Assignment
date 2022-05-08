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

x = str(input("Enter the postfix equation: "))
st = ''

print("``````Postfix to Infix``````")
for i in range(0, len(x)):
    if((ord(x[i]) >= 97 and ord(x[i]) <= 122) or (ord(x[i]) >= 65 and ord(x[i]) <= 90)):
        push(x[i])
    else:
        print(s)
        s1 = top()
        pop()
        s2 = top()
        pop()
        st = '('+  s2 + x[i] + s1 + ')'
        push(st)
inf = top()
print("Infix Expression:",inf)

# A CODE BY TUSHAR SINGH