import requests
import json
import matplotlib.pyplot as plt

url = "https://api.currencyapi.com/v3/historical?apikey=fca_live_5efcY4QpGSnweLJpvMogbxAyis26qmE1tJms7wTi&currencies=EUR%2CUSD%2CCAD&base_currency=RUB&date=2023-12-01"
response = requests.get(url)
data = response.json()
with open('file.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
    
last_updated_at = data['meta']['last_updated_at'].split('T')[0]

currencies = []
values = []
for currency, currency_data in data['data'].items():
    currencies.append(currency_data['code'])
    values.append(1 / currency_data['value'])  # значения относительно рубля (1 / значение курса)

plt.plot(currencies, values, 'o-')
plt.xlabel('Валюта')
plt.ylabel('Курс относительно рубля')
plt.title(f'Обменный курс по отношению к рублю {last_updated_at}')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()