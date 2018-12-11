def fibonacci_seq():
    number = int(input("How many fibonacci numbers you want to generate: "))

    count = 1
    seq = []

    if number <= 0:
        print("Enter a positive number")
    elif number == 1:
        seq = [1]
    elif number == 2:
        seq = [1, 1]
    else:
        seq = [1, 1]
        while count < (number - 1):
            seq.append(seq[count] + seq[count-1])
            count += 1

    return seq

print(fibonacci_seq())