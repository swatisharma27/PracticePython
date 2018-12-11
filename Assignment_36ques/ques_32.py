import random

fh = open('words.txt', 'r')
lst = fh.readlines()
word = random.choice(lst).strip()

print("Welcome to Hangman!")
initially = len(word)*'_'
print(initially)
i = 6
guess_list = []
while i != 0:
    guess = input("Guess your letter: ")
    if guess not in guess_list:
        if guess not in word.lower():
            print('Incorrect!')
            i = i-1
            print(i, "guesses left!")
            if i == 0:
                print("You loose!")
        else:
            for index in range(len(word)):
                if word[index].lower() == guess.lower():
                    initially = initially[:index] + word[index] + initially[index+1:]
            print(initially)
        guess_list.append(guess)
    else:
        print("You've already used this letter!")

    if word == initially:
        print("\nYou win!")
        print("\nYou finally guessed the word!: ", initially)
        break