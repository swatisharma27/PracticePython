import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.nytimes.com')
soup = BeautifulSoup(url.txt, 'html.parser')

search_start = soup.find_all(class_="Story-heading")

for item in search_start:
    if item.a:
        print(item.a.text.replace("\n", " ").strip())
    else:
        print(item.contents[0].strip())