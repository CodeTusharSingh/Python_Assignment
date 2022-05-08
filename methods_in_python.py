class student():
    institution = "IIPS"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def show(self):
        print("_________________________________")
        print("Marks in python:", self.a)
        print("Marks in python lab:", self.b)
        print("_________________________________")

    @classmethod
    def info(self):
        print("Class belongs to", self.institution)

    @staticmethod
    def about():
        print("This class hold the data of marks obtained by the student in python and it's lab in IIPS.")


# instance object
s1 = student(23, 22)
s2 = student(74, 77)
s3 = student(45, 52)

s1.show()
s2.show()
s3.show()

student.info()
student.about()

# A CODE BY TUSHAR SINGH