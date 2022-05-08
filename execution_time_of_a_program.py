import time
start = time.time()
def area(a):
    if(a >= 0):
        return ((22/7)*a*a)
    else:
        return print("Radius cannot be negative")


def perimeter(a):
    if (a >= 0):
        return (2*(22/7)*a)
    else:
        return print("Radius cannot be negative")

r = float(input("enter the radius: "))
print("Area of circle:", area(r))
print("Area of circle:", format(area(r),".5f"))
print("Area of circle:", round(area(r),5))
print("Perimeter of circle:", format(perimeter(r),".3f"))
end = time.time()
print("execution time of the program:",end-start)

# A CODE BY TUSHAR SINGH