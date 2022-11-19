import requests
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/IPhone'
text = requests.get(url).text.encode('utf-8').decode('ascii', 'ignore')
soup = BeautifulSoup(text, 'lxml')
table = soup.find('table', class_='wikitable')
rows = table.find_all('tr')[1:]
print(rows)
