a_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(list(filter(lambda x: x <= 5, a_list)))

num = int(input("Enter a number: "))
print(list(filter(lambda x: x <=num, a_list)))
