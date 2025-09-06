import asyncio
from g4f.client import AsyncClient
from tkinter import *
from tkinter import ttk
from tkinter import Toplevel
import requests


def open_new_window():
    new_window = Toplevel(window)
    new_window.title("Сгенерированное изображение")
    new_window.geometry("800x600")

async def main():
    client = AsyncClient()
    
    response = await client.images.generate(
        prompt=entry.get(),
        model="flux",
        response_format="url"
    )
    
    image_url = response.data[0].url
    print(f"Generated image URL: {image_url}")

asyncio.run(main())

window = Tk()
window.title("Генератор изображений ИИ")
window.geometry("400x200")

label = Label(text="Опишите изображение:")
label.pack(pady=10)

entry = Entry(width=50)
entry.pack(pady=5)

bottom = Button(text="Отправить", command=lambda: asyncio.run(main()))
bottom.pack(pady=10)


window.mainloop()