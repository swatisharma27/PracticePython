num = int(input('Enter a number: '))
list_of_divisor = []
for elements in range(1, num+1):
    if num % elements == 0:
        list_of_divisor.append(elements)

print(list_of_divisor)



