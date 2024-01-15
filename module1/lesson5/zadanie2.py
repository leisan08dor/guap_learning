#Решение:
s = 1000
v0 = 15
v1 = 10
totalSpeed = v0+v1
totalTime = s/totalSpeed
x = v0*totalTime
import tkinter
my_window = tkinter.Tk()
my_window.title('Задачи')
my_label = tkinter.Label(text=f'Скорость первого бегуна: {v0}', font=5)
my_label.pack()
my_label2 = tkinter.Label(text=f'Скорость второго бегуна: {v1}', font=5)
my_label2.pack()
my_label3 = tkinter.Label(text=f'Дистанция: {s}', font=5)
my_label3.pack()
my_label4 = tkinter.Label(text=f'''
Используя имеющиеся данные, получили:
Время бега (ч): {round(totalTime)}
Точка пересечения бегунов (км): {round(x)}''')
my_label4.pack()
my_canva = tkinter.Canvas(my_window, width=1000, height=1000,background='white', cursor='star')
my_canva.create_line(0,400,x,400,width=5,fill='yellow')
my_canva.create_line(x,400,s,400,width=5,fill='red')
my_canva.create_line(0,400,1000,400,width=5,fill='gray', dash=(10,2))
my_canva.create_text(x,350, text=f'Точка пересечения {round(x)}км')
my_canva.create_text(x//2,425, text=f'1й бегун пробежал {round(x)}км')
my_canva.create_text(x+((s-x)//2),425, text=f'2й бегун пробежал {round(totalTime*v1)}км')
my_canva.create_oval(x,390,x+20,410,width=5,fill='orange')
my_canva.pack()
my_window.mainloop()