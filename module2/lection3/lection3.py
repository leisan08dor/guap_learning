import requests

#response=requests.get('https://ya.ru/')
#print(response)

response=requests.get('https://requests.readthedocs.io/en/latest/index.html ').text
print(response)