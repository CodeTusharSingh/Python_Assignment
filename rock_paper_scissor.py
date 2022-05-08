import random

print("press 1 for rock")
print("press 2 for scissor")    
print("press 3 for paper")
n = int(input("how many rounds you want to play: "))
c = 0
d = 0
i = 0
for i in range(1,n+1):
    print("------------------")
    a = int(input("enter your choice: "))
    if(a == 1):
        print("rock")
    elif(a == 2):
        print("scissor")
    elif(a == 3):
        print("paper")
    r = random.randrange(1, 4)
    print(r)
    if(r == 1):
        print("rock")
    elif(r == 2):
        print("scissor")
    elif(r == 3):
        print("paper")
    print("------------------")
    if(a == r):
        print("draw")
        d += 1
    elif(r == 1 and a == 3):
        print("you win")
        c += 1
    elif(r == 1 and a == 2):
        print("you losse")
    elif(r == 2 and a == 3):
        print("you losse")
    elif(r == 2 and a == 1):
        print("you win")
        c += 1
    elif(r == 3 and a == 1):
        print("you win")
        c += 1
    elif(r == 3 and a == 2):
        print("you losse")
print("------------------")
if(d == n):
    print("its a draw")
if(c > n//2):
    print("you won the match")
if(c < n//2):
    print("you lost the match")

# A CODE BY TUSHAR SINGH