number = int(input("Enter a number: "))

if number > 1:
    for divisor in range(2, number):
        if (number % divisor == 0):
            print("Number is not prime!")
            break
        else:
            print("Number is prime!")
else:
    print(number +  " is not prime!")
