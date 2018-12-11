new_string = input("Enter a new string: ")
if new_string[:] == new_string[::-1]:
    print(new_string + " is a palindrome")
print(new_string + " is not a palindrome")