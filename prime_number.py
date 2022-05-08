print("---------prime number---------")
pr = int(input("enter the number you want to check for primality: "))
c = 0
if(pr == 1):
    print("1 is nither prime not composite")
for i in range(1, pr+1):
    if(pr % i == 0):
        c += 1
if(c > 2):
    print(pr, "is not a prime number")
elif(c == 2):
    print(pr, "is a prime number")

# A CODE BY TUSHAR SINGH