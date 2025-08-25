from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from tkinter import messagebox as mb

# Список доступных тегов
ALLOWED_TAGS = [
    'sleep', 'jump', 'smile', 'fight', 'black', 'white', 'red', 'siamese', 'bengal']


def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при загрузке изображения: {e}")
        return None


def open_new_window():
    tag = tag_combobox.get()
    url_with_tag = f'https://cataas.com/cat/{tag}' if tag else mb.showerror("Ошибка", "Выберите тег")
    img = load_image(url_with_tag)
    if img:
        new_window = Toplevel()
        new_window.title("Cat Image")
        new_window.geometry("600x480")
        label = Label(new_window, image=img)
        label.image = img
        label.pack()


def random_cat():
    img = load_image('https://cataas.com/cat')
    if img:
        new_window = Toplevel()
        new_window.title("Случайный котик")
        new_window.geometry("600x480")
        label = Label(new_window, image=img)
        label.image = img
        label.pack()

window = Tk()
window.title("Cats!")
window.geometry("600x520")

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить фото", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=window.destroy)

# Метка "Выбери тег"
tag_label = Label(window, text="Выбери тег")
tag_label.pack()

tag_combobox = ttk.Combobox(window, values=ALLOWED_TAGS)
tag_combobox.pack()

# Кнопка для загрузки с тегом
tag_button = Button(window, text="Загрузить картинку по тегу", command=open_new_window)
tag_button.pack(pady=10)

# Кнопка "Случайный котик"
random_button = Button(window, text="Случайный котик", command=random_cat)
random_button.pack(pady=10)

window.mainloop()