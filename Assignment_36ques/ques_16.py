import random
import string

length = int(input('enter a password length: '))
p = ''
char = string.printable

for i in range(length):
    p += random.choice(char)

print(p)