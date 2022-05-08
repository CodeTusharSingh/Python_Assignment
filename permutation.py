def factorial(a):
    i = 1
    s = 1
    while (i < a):
        i += 1
        s *= i
    return s


n = int(input("enter the total items: "))
r = int(input("enter the no. of item to be arrange: "))
print("n factorial =", factorial(n))
print("n-r factorial =", factorial(n-r))
print("permutation =", factorial(n)//factorial(n-r))

# A CODE BY TUSHAR SINGH