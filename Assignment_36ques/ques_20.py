def order_list(list1):
    list1 = sorted(list1, reverse = False)

    number = int(input("Enter a number: "))
    if number in list1:
        return True
    else:
        return False

a = list(range(1,15))
print(order_list(a))