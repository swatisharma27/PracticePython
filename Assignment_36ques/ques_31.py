import random

fh = open('words.txt', 'r')
lst = fh.readlines()
word = random.choice(lst).strip()

print("Welcome to Hangman!")
initially = len(word)*'_'
print(initially)
guess_list = []
while initially != word:
    guess = input("Guess your letter: ")
    if guess not in guess_list:
        if guess not in word.lower():
            print('Incorrect!')
        else:
            for index in range(len(word)):
                if word[index].lower() == guess.lower():
                    initially = initially[:index] + word[index] + initially[index+1:]
            print(initially)
        guess_list.append(guess)
    else:
        print("You've already used this letter!")

print("\n\nYou finally guessed the word!: ", initially)
