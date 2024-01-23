import requests
from bs4 import BeautifulSoup

url="https://mfd.ru/currency/?currency=USD"
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
data = soup.find('table', {'class': 'mfd-table mfd-currency-table'}).find_all('td')

for i in range(len(data)):
    if "USD" in data[i].text:
        usd_rate = data[i+1].text
        break

print("Курс USD:", usd_rate)