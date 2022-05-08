import functools

list1 = [2, 55, 66, 88, 77, 44, 12, 58, 99]
list_even1 = list(filter(lambda x: x % 2 == 0, list1))
list_odd1 = list(filter(lambda x: x % 2, list1))
print(list1, list_even1)
print(list1, list_odd1)
list_even2 = list(map(lambda x: x * 2, list_even1))
print(list1, list_even2)
sum = functools.reduce(lambda x, y: x + y, list_even2)
print(sum)

# A CODE BY TUSHAR SINGH