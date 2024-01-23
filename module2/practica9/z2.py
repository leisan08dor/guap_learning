import bs4
import pandas as pd

with open('module2\practica9\index.html', mode='r', encoding='utf-8') as f:
    html_text = f.read() # открыли html-файл
    
soup = bs4.BeautifulSoup(html_text, 'html.parser') # создали объект BeautifulSoup для чтения

# создали списки для продуктов и их цены
products = []
prices = []

# получили все карточки товаров с помощью find_all
card_divs = soup.find_all('div', {'class': 'card'})
# при каждом вхождении добавили название продукта и его цену в соответствующие списки
for card in card_divs:
    product = card.find('a', {'class': 'card__title'}).text
    price = card.find('div', {'class': 'card__prices'}).find('div', {'class': 'card__price card__price--common'}).text
    products.append(product)
    prices.append(price)

# заполнили дата фрейм
data = {'Product': products, 'Price': prices}
df = pd.DataFrame(data)
df_cleaned =  df.applymap(lambda x: x.strip())

print(df_cleaned)