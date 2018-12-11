import json

birthdays = {}
fh_r = open('birthdays_of_scientists.json', 'r')
birthdays = json.load(fh_r)

def add_new():
    name = input('Enter name for the new entry\n').title()
    date = input('Enter his/her birthday:\n')
    birthdays[name] = date

    fh_w = open('birthdays_of_scientists.json', 'w')
    json.dump(birthdays, fh_w)
    print('New entry added: %s' %name)

def fetch():
    print('We know the birthdays of:')
    for name in birthdays.keys():
        print(name)
    nam = input("Who's birthday do you want to look up?\n")
    if nam in birthdays:
        print(nam + "'s birthday is " + birthdays[nam])
    else:
        print("The name doesn't match with the ones we have stored.")

if __name__ == "__main__":
    print("Welcome to the birthday dictionary.")
    print("Enter 'Add' to add new entry, or 'Fetch' to fetch data:")
    usr_ip = input()
    if usr_ip == 'Add':
        add_new()
    elif usr_ip == 'Fetch':
        fetch()
