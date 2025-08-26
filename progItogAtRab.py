import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


# Функция для выгрузки списка с API
def load_currencies():
    try:
        response = requests.get("https://api.coinbase.com/v2/exchange-rates?currency=BTC")
        response.raise_for_status()
        data = response.json()
        return sorted(list(data["data"]["rates"].keys()))
    except Exception as e:
        result = mb.askyesno("Ошибка", f"Ошибка загрузки: {e}\n\nПовторить попытку?")
        if result:
            return load_currencies()


# Функция для обновления списка в случае ошибки
def retry_load():
    global cripto_list
    cripto_list = load_currencies()
    b_combobox['values'] = cripto_list
    t_combobox['values'] = cripto_list


# Основная функция для выбора двух валют и показа их курса обмена
def exchange():
    t_code = t_combobox.get().upper()
    b_code = b_combobox.get().upper()

    if t_code and b_code:
        try:
            response = requests.get(f"https://api.coinbase.com/v2/exchange-rates?currency={b_code}")
            response.raise_for_status()
            data = response.json()
            if t_code in data["data"]["rates"]:
                exchange_rate = float(data["data"]["rates"][t_code])
                mb.showinfo("Курс обмена", f"Курс обмена {exchange_rate:.2f} {t_code} за 1 {b_code}")
            else:
                mb.showerror("Ошибка", f"Криптовалюта {t_code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")
    else:
        mb.showwarning("Внимание!", "Введите код криптовалюты.")


# Функция для фильтрации списка по вводу с клавиатуры
def on_keyrelease(event):
    widget = event.widget
    current_text = widget.get().upper()
    
    # Фильтруем список по введенному тексту
    if current_text:
        filtered_list = [item for item in cripto_list if item.startswith(current_text)]
        widget['values'] = filtered_list
        
        # Обновляем текст в верхнем регистре
        if widget.get() != current_text:
            cursor_pos = widget.index(INSERT)
            widget.delete(0, END)
            widget.insert(0, current_text)
            widget.icursor(cursor_pos)
    else:
        # Восстанавливаем полный список
        widget['values'] = cripto_list

# Основное окно программы
window = Tk()
window.title("Курс обмена криптовалют")
window.geometry("400x300")

cripto_list = load_currencies()

Label(text="Базовая криптовалюта").pack(padx=10, pady=10)

b_combobox = ttk.Combobox(values=cripto_list, state='normal')
b_combobox.pack(padx=10, pady=10)
b_combobox.bind('<KeyRelease>', on_keyrelease)

Label(text="Целевая криптовалюта").pack(padx=10, pady=10)

t_combobox = ttk.Combobox(values=cripto_list, state='normal')
t_combobox.pack(padx=10, pady=10)
t_combobox.bind('<KeyRelease>', on_keyrelease)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=5)
Button(text="Обновить списоки криптовалют", command=retry_load).pack(padx=10, pady=5)

window.mainloop()
