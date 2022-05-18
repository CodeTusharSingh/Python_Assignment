# x = range(0,100,50)
# for i in x:
# print(i)

a = int(input("enter the value you want to print the table of :: "))
p = 1
for i in range(a, (a*10)+1, a):
    print("{} * {} = {}".format(a, p, i))
    p += 1

# a = [8,9,6,3]
# print(a)
# sum = 0
# for i in a:
#     sum = sum + i
# print(sum)