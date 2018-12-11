import random

a = random.sample(range(1,90), 15)
b = random.sample(range(1,50), 20)

output = [element for element in set(a) if element in b]
print(output)
