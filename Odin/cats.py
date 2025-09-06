from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import requests
from io import BytesIO
from tkinter import Toplevel

Allowed_tags = ["sleep", "jump", "fight", "black", "white", "bengal", "siamese", "cute"]


def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        img_data = BytesIO(response.content)
        img = Image.open(img_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Произошла ошибка {e}")
        return None


def open_new_window():
    tag = tag_combobox.get()
    url_tag = f"http://cataas.com/cat/{tag}" if tag else "http://cataas.com/cat"
    img = load_image(url_tag)
    if img:
        new_window = Toplevel()
        new_window.title("Котик")
        new_window.geometry("600x480")
        label = Label(new_window, image = img)
        label.pack()
        label.image = img


window = Tk()
window.title("Котики!")
window.geometry("300x200")

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить картинку", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=window.destroy)

url = "http://cataas.com/cat"

tag_label = Label(text="Выбери тег:")
tag_label.pack()

tag_combobox = ttk.Combobox(values=Allowed_tags)
tag_combobox.pack()

load_button = Button(text="Загрузить", command=open_new_window)
load_button.pack(pady=10)


window.mainloop()
