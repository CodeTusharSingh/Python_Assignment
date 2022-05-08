print("<<<<<-----------Calculator----------->>>>>")

# function for addition


def addition(a, b):
    return (a + b)

# function for subtraction


def subtraction(a, b):
    return (a - b)

# function for multiplication


def multiplication(a, b):
    return (a * b)

# function for division


def division(a, b):
    # division by zero is not possible
    if (b == 0):
        print("Division by zero is not possible!!!!!")
    else:
        return (a / b)

# function for modulo


def modulo(a, b):
    # division by zero is not possible
    if (b == 0):
        print("Division by zero is not possible!!!!!")
    else:
        return (a % b)
# function for square


def square(a):
    if(a == 1):
        return 1
    elif(a == 0):
        return 0
    else:
        return (a*a)
# function for cube


def cube(a):
    if(a == 1):
        return 1
    elif(a == 0):
        return 0
    else:
        return (a*a*a)
# function for square root


def sqrt(a):
    if(a == 0):
        return 0
    elif(a == 1):
        return 1
    else:
        return a ** (0.5)
# function for cube root


def cubet(a):
    if(a == 0):
        return 0
    elif(a == 1):
        return 1
    else:
        return a ** (1/3)


def checki(a):  # for integer value
    # checking for invalid input using ascii values
    # for loop is used to check if there is a invalid input given by the user
    # for loop is used to check multiple characters
    for i in a:
        # the ascii values of 0 to 9 is from 48 to 57 so except these values all the other values are invalid to be considered as a integer
        # '.'(ascii value = 46) is invalid for a integer but valid for float
        if(0 <= ord(i) and 47 >= ord(i)):
            # if this condition is true the exit the program
            # one thing to keep in mind is that '-'(ascii value = 45) and '+'(ascii value = 43) can also be accepted as integer & float if they are at correct position i.e. at the beginning of any number for example: -8,-96,+96 are all valid but 8-,96+ are invalid
            if(a[0] == '-' or a[0] == '+'):
                # if the above condition is true then use the continue statement
                if(ord(i) == 45 or ord(i) == 43):
                    continue
            print("Invalid Input!!!")
            exit()
        elif(58 <= ord(i) and 127 >= ord(i)):
            # if this condition is true the exit the program
            print("Invalid Input!!!")
            exit()


def checkf(a):  # for float value
    for k in a:
        if(0 <= ord(k) and 47 >= ord(k)):
            if(a[0] == '-' or a[0] == '+'):
                if(ord(k) == 45 or ord(k) == 43):
                    continue
                if(ord(k) == 46):
                    continue
            print("Invalid Input!!!")
            exit()
        elif(58 <= ord(k) and 127 >= ord(k)):
            print("Invalid Input!!!")
            exit()


print("-----------------------------------------------")
n = int(input("Enter how many times you want to perform the calculations: "))
for i in range(0, n):
    print("-----------------------------------------------")
    print("Enter i or I if you want to input a integer value")
    print("Enter f or F if you want to input a float value")
    print("-----------------------------------------------")
    print("Enter u or U for unary operator")
    print("Enter b or B for binary operator")
    print("-----------------------------------------------")
    print("Enter '+' for addition")
    print("Enter '-' for subtraction")
    print("Enter '*' for multiplication")
    print("Enter '/' for division")
    print("Enter '%' for modulo")
    print("Enter '^' for power")
    print("Enter 'root' for power")
    print("-----------------------------------------------")
    choice3 = str(
        input("Enter the choice for unary or binary operator (u or U or b or B): "))
    choice1 = str(
        input("Enter the choice for integer or float(i or I or f or F): "))
    if(choice3 == 'b' or choice3 == 'B'):
        choice2 = str(
            input("Enter your choice for arthmetic operation(+,/,*,-,%): "))
    elif(choice3 == 'u' or choice3 == 'U'):
        choice2 = str(
            input("Enter your choice for arthmetic operation(^,root): "))
    else:
        print("Invalid Input!!!")
        exit()

    print("-----------------------------------------------")
    if(choice3 == 'b' or choice3 == 'B'):
        # if user chooses i or I then this condition is true
        if(choice1 == 'i' or choice1 == 'I'):
            a1 = (input("Enter the first integer: "))
            checki(a1)
            # convert the valid string into integer
            a1 = int(a1)
            # the same process goes for second variable
            b1 = (input("Enter the second integer: "))
            print("-----------------------------------------------")
            checki(b1)
            b1 = int(b1)
            # the choice for arthmetic operation is given by the user so use the appropriate function according to the operator
            if(choice2 == '+'):
                print(a1, "+", b1, "=", addition(a1, b1))
            elif(choice2 == '-'):
                print(a1, "-", b1, "=", subtraction(a1, b1))
            elif(choice2 == '*'):
                print(a1, "*", b1, "=", multiplication(a1, b1))
            elif(choice2 == '/'):
                # this condition is for zero division
                if(b1 == 0):
                    division(a1, b1)
                else:
                    print(a1, "/", b1, "=", division(a1, b1))

            elif(choice2 == '%'):
                # this condition is for zero division
                if(b1 == 0):
                    modulo(a1, b1)
                else:
                    print(a1, "%", b1, "=", modulo(a1, b1))
        # if user chooses f or F then this condition is true
        # all the conditions is same as of integer just keep in mind that '.'(ascii value = 46) is valid in float
        elif(choice1 == 'f' or choice1 == 'F'):
            a2 = (input("Enter the first integer: "))
            checkf(a2)
            a2 = float(a2)
            b2 = (input("Enter the second integer: "))
            print("-----------------------------------------------")
            checkf(b2)
            b2 = float(b2)
            if(choice2 == '+'):
                print(a2, "+", b2, "=", addition(a2, b2))
            elif(choice2 == '-'):
                print(a2, "-", b2, "=", subtraction(a2, b2))
            elif(choice2 == '*'):
                print(a2, "*", b2, "=", multiplication(a2, b2))
            elif(choice2 == '/'):
                if(b2 == 0):
                    division(a2, b2)
                else:
                    print(a2, "/", b2, "=", division(a2, b2))
            elif(choice2 == '%'):
                if(b2 == 0):
                    modulo(a2, b2)
                else:
                    print(a2, "%", b2, "=", modulo(a2, b2))
        # if user nither chooses i or I or f or F then print a message
        else:
            print("Invalid Input!!!")
        print("-----------------------------------------------")
    elif(choice3 == 'u' or choice3 == 'U'):
        if(choice1 == 'i' or choice1 == 'I'):
            a3 = (input("Enter the integer: "))
            checki(a3)
            a3 = int(a3)
            if(choice2 == '^'):
                power = (input("Enter the power(2 or 3): "))
                checkf(power)
                power = int(power)
                if(power == 0):
                    print(a3, "^", power, "= 1")
                elif(power == 2):
                    print(a3, "^", power, "=", square(a3))
                elif(power == 3):
                    print(a3, "^", power, "=", cube(a3))
            elif(choice2 == 'root'):
                rt = input("Enter the root(2 or 3): ")
                checki(rt)
                rt = int(rt)
                if(rt == 2):
                    print("Sqr root(", a3, ") =", sqrt(a3))
                elif(rt == 3):
                    print("Cube root(", a3, ") =", cubet(a3))
        elif(choice1 == 'f' or choice1 == 'F'):
            a4 = (input("Enter the float: "))
            checkf(a4)
            a4 = float(a4)
            if(choice2 == '^'):
                power = (input("Enter the power(2 or 3): "))
                power = int(power)
                if(power == 0):
                    print(a4, "^", power, "= 1")
                elif(power == 2):
                    print(a4, "^", power, "=", square(a4))
                elif(power == 3):
                    print(a4, "^", power, "=", cube(a4))
            elif(choice2 == 'root'):
                rt = input("Enter the value of root(2 or 3): ")
                rt = int(rt)
                if(rt == 2):
                    print("Sqr root(", a4, ") =", sqrt(a4))
                elif(rt == 3):
                    print("Cube root(", a4, ") =", cubet(a4))
        # if user nither chooses i or I or f or F then print a message
        else:
            print("Invalid Input!!!")
    else:
        print("Invalid Input!!!")

# A CODE BY TUSHAR SINGH