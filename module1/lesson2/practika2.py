#ввод a,b,c
#вывод a^(b+c)

# a,b,c = float(input()),float(input()),float(input())
# print(a**(b+c))
print('Введите ваше имя:')
name = input()
print('Введите ваш возраст:')
age = input()
print('Знаетеле ли вы питон (да/нет):')
answer = input()
message=f'Мое имя {name} \n мне {age} года \n я знаю питон {answer}'
print(message)


my_name=str(input('Имя:'))
my_age=int(input('Возраст:'))
my_expiriance=bool(input('Знаешь ли python?'))

message=f'Мое имя {my_name} \n мне года {my_age} \n я знаю питон {my_expiriance}'
print(message)

# in : a,b 
# out : a или b
a = int(input())
b = int(input())
print(((a>b)*a)+(((a<b)*b)))

