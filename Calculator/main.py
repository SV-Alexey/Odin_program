from tkinter import *
from tkinter import ttk
import calculator_logic as c
from tkinter import messagebox as mb

#  Основная функция
def calc():
    num2 = float(entry.get())
    if oper == '+':
        result = c.add(num1, num2)
    elif oper == '-':
        result = c.subtract(num1, num2)
    elif oper == '*':
        result = c.multiply(num1, num2)
    elif oper == '/':
        try:        
            result = c.divide(num1, num2)
        except ZeroDivisionError:
            entry.delete(0, END)
            mb.showerror("Ошибка", "На ноль делить нельзя!")
            entry.focus()
            return
    elif oper == 'x²':
        result = c.square(num1)
    entry.delete(0, END)

    if result == int(result):       # Убираем .0 если результат целое число
        entry.insert(0, str(int(result)))
    else:
        entry.insert(0, str(result))
    entry.focus()


def enter_number(number):
    entry.insert(END, number)
    entry.focus()


def clear_entry():
    entry.delete(0, END)
    entry.focus()


def set_operation(operation):
    global num1
    global oper
    num1 = float(entry.get())
    oper = operation
    entry.delete(0, END)
    entry.focus()


#  Отдельная функция для x², что бы сразу выводить результат
def square_calc(operation):
    num = float(entry.get())
    if operation == 'x²':
        result = c.square(num)
    entry.delete(0, END)
    if result == int(result):
        entry.insert(0, str(int(result)))
    else:
        entry.insert(0, str(result))
    entry.focus()


#  Функция для корректного ввода
def validate_entry():
    e = entry.get()
    txt = ''.join(b for b in e if b in "0123456789.-")
    if len(txt) > 1 and txt.endswith('-'):      # Запрет на ввод минуса после числа
        txt = txt[:-1]  
    if e != txt:
        entry.delete(0, END)
        entry.insert(0, txt)
    
#  Графический интерфейс
window = Tk()
window.title("Калькулятор")

#  Поле ввода
entry = ttk.Entry()
entry.grid(row=0, column=0, columnspan=4, sticky='ew')
entry.focus()
entry.bind('<KeyRelease>', lambda event: validate_entry())

#  Кнопки с цифрами
ttk.Button(text='1', command=lambda: enter_number('1')).grid(row=1, column=0)
ttk.Button(text="2", command=lambda: enter_number('2')).grid(row=1, column=1)
ttk.Button(text="3", command=lambda: enter_number('3')).grid(row=1, column=2)
ttk.Button(text="4", command=lambda: enter_number('4')).grid(row=2, column=0)
ttk.Button(text="5", command=lambda: enter_number('5')).grid(row=2, column=1)
ttk.Button(text="6", command=lambda: enter_number('6')).grid(row=2, column=2)
ttk.Button(text="7", command=lambda: enter_number('7')).grid(row=3, column=0)
ttk.Button(text="8", command=lambda: enter_number('8')).grid(row=3, column=1)
ttk.Button(text="9", command=lambda: enter_number('9')).grid(row=3, column=2)
ttk.Button(text="0", command=lambda: enter_number('0')).grid(row=4, column=1)

#  Кнопки с операциями
ttk.Button(text="C", command=clear_entry).grid(row=4, column=0)
ttk.Button(text="=", command=calc).grid(row=4, column=2)
ttk.Button(text="+", command=lambda: set_operation('+')).grid(row=1, column=3)
ttk.Button(text="-", command=lambda: set_operation('-')).grid(row=2, column=3)
ttk.Button(text="*", command=lambda: set_operation('*')).grid(row=3, column=3)
ttk.Button(text="/", command=lambda: set_operation('/')).grid(row=4, column=3)
ttk.Button(text="x²", command=lambda: square_calc('x²')).grid(row=5, column=0)

window.mainloop()