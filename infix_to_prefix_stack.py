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

print("``````Infix to Prefix``````")
x = x[::-1]
print(x)
for i in range(0, len(x)):
    if(x[i] == '0' or x[i] == '1' or x[i] == '2' or x[i] == '3' or x[i] == '4' or x[i] == '5' or x[i] == '6' or x[i] == '7' or x[i] == '8' or x[i] == '9'):
        st += x[i]
    elif(x[i] == ')'):
        push(x[i])
    elif(x[i] == '('):
        while(empty() == False and top() != ')'):
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
st = st[::-1]
print("Prefix expression:", st)

# A CODE BY TUSHAR SINGH