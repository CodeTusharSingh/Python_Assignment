class overloaing:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        r = self.x + other.x
        return r


ob1 = overloaing(1)
ob2 = overloaing(3)
ob3 = overloaing("Tushar ")
ob4 = overloaing("Singh")
print(ob1 + ob2)
print(ob3 + ob4)

# A CODE BY TUSHAR SINGH