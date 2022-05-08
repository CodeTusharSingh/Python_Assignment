a = int(input("enter the value you want to print the table of :: "))
p = 1
for i in range(a, (a*10)+1, a):
    #    print(a,"*",p,"=",i)
    print("{} * {} = {}".format(a, p, i))
    p += 1

# A CODE BY TUSHAR SINGH