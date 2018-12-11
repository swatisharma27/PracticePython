import json
import calendar

birthdays = {}
fh_r = open('birthdays_of_scientists.json', 'r')
birthdays = json.load(fh_r)

lst = []
for bday in birthdays.values():
    lst.append(calendar.month_name[int(bday.split('/')[0])])

dict = {}

for k in lst:
    if k in dict:
        dict[k] = dict[k] + 1
    else:
        dict[k] = 1

print(dict)
