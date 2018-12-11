import random
import time

print("Welcome to the Guessing Game!")
print("\nThere is a number in my head between 0 and 100\n")
min=0
max=100
mid = 50
number_in_my_head = 40
# Initial guess
guess = mid
print("Guess a number, program: ")
time.sleep(5)
print(guess)
count = 1

while guess != number_in_my_head:
    if guess < number_in_my_head:
        print("It is too low!")
        min = guess + 1
        print("Guess again: ")
        time.sleep(5)
        guess = random.randint(min, max)
        print(guess)
        count = count + 1
    elif guess > number_in_my_head:
        print("It is too high!")
        max = guess - 1
        print("Guess again: ")
        time.sleep(5)
        guess = random.randint(min, max)
        print(guess)
        count = count + 1

print("\n\nHurray! You took", count, " guesses to guess the number in my head!")