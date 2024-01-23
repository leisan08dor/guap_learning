import requests
import json

url = "https://api.currencyapi.com/v3/historical?apikey=fca_live_5efcY4QpGSnweLJpvMogbxAyis26qmE1tJms7wTi&currencies=USD&base_currency=RUB&date=2024-01-18"
response = requests.get(url)
data = response.json()
with open('file.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
print(json.dumps(data, indent=4))