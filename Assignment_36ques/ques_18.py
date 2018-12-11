number = input('Enter a 4-digit number: ')
cows = 0
bulls = 0

if len(number) == 4:
    guess = input('Take a guess 4-digit number: ')
    new = []
    if len(number) == len(guess):
        list1 = list(number)
        print(list1)
        list2 = list(guess)
        print(list2)
        for i in list1:
            if i in list2:
                if list1.index(i) == list2.index(i):
                    cows += 1
                else:
                    bulls += 1

print(cows, " cows, ", bulls, " bulls")