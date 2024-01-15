#Задача 1:
#Создать окно и рабочую область размером не менее 500*500рх
#Задать заголовок рабочего окна
#Создать метку с названием "Конкурс"

#Решение:
import tkinter
my_window = tkinter.Tk()
my_window.title('Задание 1')
my_label = tkinter.Label(text='Конкурс', font=10)
my_label.pack()
my_canva = tkinter.Canvas(my_window, width=750, height=750,background='yellow', cursor='star')

my_canva.pack()
my_window.mainloop()