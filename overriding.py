class a:
    def random(self):
        print("HELLO A")
class c:
    def random(self):
        print("HELLO C")
class b(a,c):
    def random(self):
        print("HELLO B")

item1 = b()
item2 = a()
item3 = c()
item1.random()
item2.random()
item3.random()

from cmath import pi


class area:
    def __init__(self, a, b, c = 0):
        self.a = a
        self.b = b
        self.c = c

    def ar(self, a=None, b=None):
        if(a != None and b == None):
            return pi * a * a
        elif(a != None and b != None):
            return a * b
        else:
            return 0


s = area(5, 2)
print("Area of circle:", s.ar(7))
print("Area of rectangle:", s.ar(7, 2))
