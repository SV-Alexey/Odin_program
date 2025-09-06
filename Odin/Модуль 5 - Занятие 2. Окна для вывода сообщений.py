from tkinter import *
from tkinter import messagebox as mb

def pr():
    try:
        s1 = int(e1.get())
        s2 = int(e2.get())
        s3 = int(e3.get())
        m1["text"] = f"{s1} * {s2} * {s3} = {s1 * s2 * s3}"
        answer = mb.askretrycancel("Вопрос", "Попробовать еще?")
        if answer == False:
            window.destroy()
        else:
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            m1["text"] = ""
    except ValueError:
        mb.showerror("Ошибка", "Введены не числа")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)

def summ():
    try:
        s1 = int(e1.get())
        s2 = int(e2.get())
        s3 = int(e3.get())
        m1["text"] = f"{s1} + {s2} + {s3} = {s1 + s2 + s3}"
        answer = mb.askretrycancel("Вопрос", "Попробовать еще?")
        if answer == False:
            window.destroy()
        else:
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            m1["text"] = ""
    except ValueError:
        mb.showerror("Ошибка", "Введены не числа")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)

window = Tk()
window.title("Калькулятор")
cx = (window.winfo_screenwidth() // 2) - (800 // 2)
cy = (window.winfo_screenheight() // 2) - (400 // 2)
window.geometry(f"300x200+{cx}+{cy}")
m = Label(text="Введите 3 целых числа")
m.pack()

e1 = Entry()
e1.pack()
e2 = Entry()
e2.pack()
e3 = Entry()
e3.pack()
b = Button(text = "Сложить три числа", command = summ)
b.pack()
p = Button(text = "Умножить три числа", command = pr)
p.pack()
m1 = Label()
m1.pack()

window.mainloop()