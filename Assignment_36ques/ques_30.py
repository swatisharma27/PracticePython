import random

fh = open('words.txt', 'r')
lst = fh.readlines()
print(random.choice(lst).strip())
