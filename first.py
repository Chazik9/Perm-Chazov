import sqlite3
from tkinter import *
from tkinter import ttk


a = 0
count = 5
conn = sqlite3.connect('orda.db')
cur = conn.cursor()



def vivod():
    cur.execute("SELECT * FROM users;")
    all_results = cur.fetchall()
    for person in all_results:
        tree.insert("", END, values=person)

def new():
    global count
    count += 1
    b = []
    b.append(count)
    w1.deiconify()
    b1 = entry1.get()
    b2 = entry2.get()
    b.append(b1)
    b.append(b2)
    cur.execute("INSERT INTO users VALUES(?, ?, ?);", b)
    conn.commit()
    
    
        
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
w1 = Tk()
w1.geometry("250x200")
w1.withdraw()
entry1 = Entry(w1)
entry1.pack(anchor=NW, padx=6, pady=6)
entry2 = Entry(w1)
entry2.pack(anchor=NW, padx=6, pady=6)
btn_1 = Button(root,text="Кнопка", command=new)
btn_1.pack()
 
# опреде
 
# определяем столбцы
columns = ("id", "Ang", "Rus")
 
tree = ttk.Treeview(columns=columns, show="headings")
tree.pack(fill=BOTH, expand=1)
 
# определяем заголовки
tree.heading("id", text="id", anchor=W)
tree.heading("Ang", text="Ang", anchor=W)
tree.heading("Rus", text="Rus", anchor=W)


tree.column("#1", stretch=NO, width=70)
tree.column("#2", stretch=NO, width=60)
tree.column("#3", stretch=NO, width=100)
 
vivod()
 
root.mainloop()

cur.execute("SELECT * FROM users;")
all_results = cur.fetchall()



count += 1
        b = []
        b.append(count)
        b1 = input('Ведите Англисоке слово ')
        b2 = input('Ведите Русское слово ')
        b.append(b1)
        b.append(b2)
        cur.execute("INSERT INTO users VALUES(?, ?, ?);", b)
        conn.commit()
        text()
    
    if a == 2:
        b3 = input('Ведите Номер слово, которе надо удалить ')
        try:
            cur.execute("Delete from users Where userid =?;", b3)
        except:
            print("Ошибка запроса")
        conn.commit()
        text()
    if a == 3:
        print('Программа завершена')
    
    


        
  




