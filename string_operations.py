a = "Do geese see God"
print(len(a))
print(a.upper())
print(a.lower())
print(a.title())
print(a.capitalize())
print(a.center(24, '$'))
print(a.count(' '))
a = a.casefold()
z = reversed(a)
if list(a) == list(z):
    print("palindrome")
else:
    print("not palindrome")
print(a.endswith('God', 0, 17))
print(a[13:16])
print(a[-16:-1])
print(a[0:16:2])
a = a.replace("geese", "birds")
print(a)
print(a.find('r'))

# A CODE BY TUSHAR SINGH