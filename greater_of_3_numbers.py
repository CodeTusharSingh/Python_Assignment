a = int(input("Enter the first value (a) :: "))
b = int(input("Enter the second value (b) :: "))
c = int(input("Enter the third value (c) :: "))

if(a == b == c):
    print("all the values are equal")
elif(a == b and a < c and b < c):
    print("a and b are equal and c is greater than a and b")
elif(c == b and c < a and b < a):
    print("c and b are equal and  a is greater than c and b")
elif(c == a and a < b and c < b):
    print("c and a are equal and  b is greater than c and a")
elif(a == b and a > c and b > c):
    print("a and b are equal and greater than c")
elif(c == b and c > a and b > c):
    print("c and b are equal and greater than a")
elif(c == a and c > b and a > b):
    print("c and a are equal and greater than b")
elif(a > b and a > c):
    print("a is greater than b and c")
elif(b > c and b > a):
    print("b is greater than a and c")
elif(c > b and c > a):
    print("c is greater than a and b")

# A CODE BY TUSHAR SINGH