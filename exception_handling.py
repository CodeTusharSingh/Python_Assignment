try:
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = a / b
    print("{} / {} = {}".format(a, b, c))
except ZeroDivisionError:
    print("Denominator cannot be zero")
except ValueError:
    print("Please provide a integer value")

# A CODE BY TUSHAR SINGH