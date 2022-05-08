print("BY RECURSION")
def fibonacci(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    elif(n > 1):
        return fibonacci(n-2)+fibonacci(n-1)


n = int(input("enter the limit of the fibonacci series: "))
for i in range(0,n):
    print(fibonacci(i), end = ' ')
print()

print("------------------------------------------------")

print("BY ITERATION")
a = 0
b = 1
c = a + b
n1 = int(input("enter the limit of the fibonacci series: "))
print(a)
print(b)
for i in range(3, n1+1):
    print(c)
    a = b
    b = c
    c = a + b

# A CODE BY TUSHAR SINGH