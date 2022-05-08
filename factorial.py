print("BY RECURSION")
def fact(n):
    if(n>0):
        return n*fact(n-1)
    elif(n==0):
        return 1
n = int(input("enter the number you want to find out the factorial of: "))
fact_val = fact(n)
print("Factorial of {} is: {}".format(n,fact_val))

print("------------------------------------------------")

print("BY ITERATION")
n1 = int(input("enter the number you want to find out the factorial of: "))
i = 1
s = 1
while(i < n1):
    i = i + 1
    s = s * i
print("Factorial of {} is: {}".format(n1,s))

# A CODE BY TUSHAR SINGH