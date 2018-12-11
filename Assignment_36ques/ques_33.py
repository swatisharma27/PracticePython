birthdays = {'Albert Einstein': '03/14/1879', 'Benjamin Franklin': '01/17/1706', 'Ada Lovelace': '12/10/1815'}
print('Welcome to the birthday dictionary. We know the birthdays of:')
for name in birthdays.keys():
    print(name)
nam = input("Who's birthday do you want to look up?\n")
if nam in birthdays:
    print(nam + "'s birthday is " + birthdays[nam])
else:
    print("The name doesn't match with the ones we have stored.")
