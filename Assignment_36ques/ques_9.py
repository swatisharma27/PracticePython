print('Game is to guess the number')
number = int(input('Enter a number between 1 or 9: '))

guess = 0
count = 0

while guess != number and guess != "exit":
    guess = int(input("Take a guess: "))
    if guess == "exit":
        print("game ended")
        break

    count += 1
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print("Right Guess! You won!")
        print("It took counts: ", count)

