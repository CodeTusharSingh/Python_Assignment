class cube:
    def __init__(self,s):
        self.s = s
    def area(self):
        return (6 * self.s ** 2)
    def volume(self):
        return (self.s ** 3)
    def perimeter(self):
        return (self.s * 12)
s = int(input("Enter the side of cube: "))
c = cube(s)
a = c.area()
p = c.perimeter()
v = c.volume()
print("Area of the cube: ", a)
print("Perimeter of the cube: ", p)
print("Volume of the cube: ", v)

# A CODE BY TUSHAR SINGH