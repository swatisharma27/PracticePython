with open('happynumbers.txt', 'r') as hn:
    happyNumbers = hn.split('\n')

with open('primarynumbers.txt', 'r') as pn:
   primeNumbers = pn.read().split('\n')


for element in primeNumbers:
    if element in happyNumbers:
            print(element)

