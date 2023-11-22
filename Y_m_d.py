#Дана дата в формате 'Y-m-d'
#Преобазовать ее в словарь типа:
#{'year':'Y','month':'M','day':'d'}

#Решение:
date='2023-11-22'.split('-')
dict={'year':date[0],'month':date[1],'day':date[2]}
print(dict)
