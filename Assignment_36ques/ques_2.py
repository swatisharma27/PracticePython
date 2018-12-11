num = int(input('Enter a number to check: '))
check = int(input('Enter the number to divide by: '))

if num%check == 0 and num%4 == 0:
    print("It is multiple of 4.")
elif num%check == 0:
    print("It is an even number.")
else:
    print("It is an odd number.")

