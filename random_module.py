import random
a = random.sample(range(1,30), 12)
print(a)
b = random.sample(range(1,30), 16)
print(b)
result = [i for i in set(a) if i in b]
print(result)