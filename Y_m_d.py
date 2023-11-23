#Дана дата в формате 'Y-m-d'
#Преобазовать ее в словарь типа:
#{'year':'Y','month':'M','day':'d'}

#Решение:
def conv_dict(date):
    date=date.split('-')
    dict={'year':date[0],'month':date[1],'day':date[2]}
    return dict
try:
    date=input('Введите дату в формате: Год-месяц-день\n')
    result=conv_dict(date)
    print(result)  
except:
    print('Ошибка! Проверьте вводимые данные.')


