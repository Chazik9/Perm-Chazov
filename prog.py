from tkinter import*
from tkinter import simpledialog

names = []
answer1 = 0

window = Tk()
window.geometry('280x200')


def cl(event):
    global a, b, op
    a=0
    b=0
    op=0
    lab['text'] = '0'
def otv():
    global names
    
    lab = Label(text='', font=("Arial", 18))
    lab.pack()
    lab.place(x=10, y=10)

def name():
    global names, answer1
    for i in range(answer1):
        name1 = simpledialog.askstring("Input", f"Как зовут {i + 1} ученика?",
                                parent=window)
        names.append(name1)
        

def start(event):
    global answer1
    answer1 = simpledialog.askinteger("Input", "Сколко учеников в классе?",
                                 parent=window,
                                 minvalue=1, maxvalue=100)
    name()
import random

print(f'рандомный лох вашего класса {random.choice(v)}')

        

lab = Label(text='Кто сегодня дежурный?', font=("Arial", 18))
lab.pack()
lab.place(x=10, y=10)

btnstart = Button(text='Начать', width = 35, height = 2)
btnstart.pack()
btnstart.place(x=10, y=40)
btnstart.bind('<Button-1>', start)

window.mainloop()
