n = int(input("enter a number to check whether it is a armstrong number or not: "))
i = 0
sum = 0
c = n
if(n >= 1000):
    while(c != 0):
        t = c % 10
        sum = sum + (t*t*t*t)
        c = c//10
else:
    while(c != 0):
        r = c % 10
        sum = sum + (r*r*r)
        c = c//10

if(sum == n):
    print(n, "is a armstrong number")
else:
    print(n, "is not a armstrong number")

# A CODE BY TUSHAR SINGH