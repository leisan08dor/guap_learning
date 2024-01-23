import requests
from bs4 import BeautifulSoup

url="https://mfd.ru/currency/?currency=USD"
r = requests.get(url)


soup = BeautifulSoup(r.text, 'html.parser')
data = soup.find('table', {'class': 'mfd-table mfd-currency-table'}).find_all('td')
print(data)