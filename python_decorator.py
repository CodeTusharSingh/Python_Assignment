def div(x, y):
    return x / y


def smart_div(func):
    def inner(m,n):
        if m < n:
            m,n = n,m
        return func(m,n)
    return inner


a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = div(a,b)
div1 = smart_div(div)
d = div1(a,b)

print("a = ",a)
print("b = ",b)
print("c = ",c)
print("d = ",d)

# A CODE BY TUSHAR SINGH