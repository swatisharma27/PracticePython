import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture')
soup = BeautifulSoup(url.content, 'html.parser')

search_1 = soup.find_all('div', {"class:", "dek"})

for tag1 in search_1:
    print(tag1.txt)

search_2 = soup.find_all('section', {"class:", "content-selection"})
for tag2 in search_2:
    print(tag2.txt)

