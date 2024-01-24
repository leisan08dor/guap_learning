import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('module2\practica4\staff.csv')
pd.set_option('display.max_columns', None)

df['Experience'] = np.random.randint(1, 10, len(df))
companies = ['Яндекс', 'Сбер', 'ВТБ', 'IT now']
company_distribution = np.random.choice(companies, size=len(df))
df['Company'] = company_distribution
df.to_csv('staff_pro.csv')

position_experience = df.groupby(['Company', 'Position'])['Experience'].mean().reset_index()

plt.figure(figsize=(10, 6))
positions = position_experience['Position'].unique()

for position in positions:
    data = position_experience[position_experience['Position'] == position]
    plt.bar(data['Company'], data['Experience'], label=position)

plt.xlabel('Компания')
plt.ylabel('Средний опыт')
plt.title('Средний опыт работы в разрезе по должности и компании')
plt.legend()
plt.show()