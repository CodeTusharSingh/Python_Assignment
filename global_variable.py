count = 1


def plus():
    global count
    count += 1


def minus():
    global count
    count -= 1


print("Count =", count)
plus()
plus()
minus()
minus()
print("Count =", count)

# A CODE BY TUSHAR SINGH