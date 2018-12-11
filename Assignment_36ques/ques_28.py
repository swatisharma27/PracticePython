def max_of_three():
    var_1 = int(input('Enter the variable_1: '))
    var_2 = int(input('Enter the variable_2: '))
    var_3 = int(input('Enter the variable_3: '))

    if var_1 > var_2:
        if var_1 > var_3:
            return (var_1, "Variable 1 is the greatest")
        else:
            return (var_3, "Variable 3 is the greatest")
    elif var_2 > var_1:
        if var_2 > var_3:
            return (var_2, "Variable 2 is the greatest")
        else:
            return (var_3, "Variable 3 is the greatest")


print(max_of_three())
