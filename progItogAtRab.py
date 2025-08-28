import requests                                                          # Импорт библиотеки для HTTP-запросов
import json                                                              # Импорт библиотеки для работы с JSON (не используется)
from tkinter import *                                                    # Импорт всех элементов библиотеки для создания GUI
from tkinter import messagebox as mb                                     # Импорт модуля для сообщений (окна с уведомлениями)
from tkinter import ttk                                                  # Импорт современных виджетов (Combobox, кнопки и т.д.)


# Функция для загрузки списка валют с API Coinbase
def load_currencies():                                                   # Определяем функцию для загрузки списка валют
    try:                                                                 # Начинаем блок обработки исключений
        response = requests.get("https://api.coinbase.com/v2/exchange-rates")  # Отправляем GET-запрос к API Coinbase для получения курсов валют
        response.raise_for_status()                                      # Проверяем статус ответа, вызываем исключение при ошибке HTTP
        data = response.json()                                           # Преобразуем JSON-ответ в словарь Python
        return sorted(list(data["data"]["rates"].keys()))               # Извлекаем ключи валют, преобразуем в список и сортируем по алфавиту
    except Exception as e:                                               # Ловим любые исключения (ошибки сети, JSON и т.д.)
        result = mb.askyesno("Ошибка", f"Ошибка загрузки: {e}\n\nПовторить попытку?")  # Показываем диалог с вопросом о повторе
        if result:                                                       # Если пользователь нажал "Да"
            return load_currencies()                                     # Рекурсивно вызываем функцию снова (повтор попытки)
        else:                                                            # Если пользователь нажал "Нет"
            # Возвращаем резервный список популярных валют
            return ["BTC", "ETH", "USDT", "XRP", "TONE", "SOL", "TRX", "DOT", "ADA", "USD", "RUB", "EUR"]  # Список основных криптовалют и фиатных валют


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
                mb.showinfo("Курс обмена", f"Курс обмена: 1 {b_code} = {exchange_rate:.2f} {t_code}")
            else:
                if t_code not in cripto_list and b_code not in cripto_list:
                    mb.showerror("Ошибка", f"Криптовалюта {t_code} и {b_code} не найдены")
                elif t_code not in cripto_list:
                    mb.showerror("Ошибка", f"Криптовалюта {t_code} не найдена")
                elif b_code not in cripto_list:
                    mb.showerror("Ошибка", f"Криптовалюта {b_code} не найдена")
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
Button(text="Обновить список криптовалют", command=retry_load).pack(padx=10, pady=5)

window.mainloop()
