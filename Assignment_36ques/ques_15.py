word = input("Enter a string: ")

def reverse(x):
    x = word.split()
    rev_word = ' '.join(x[::-1])
    return rev_word

print(reverse(word))