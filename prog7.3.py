import asyncio
import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
from g4f.client import AsyncClient
import requests
from PIL import Image, ImageTk
from io import BytesIO
import threading

class AIImageGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор изображений ИИ")
        self.root.geometry("400x200")
        
        # Поле ввода
        tk.Label(root, text="Опишите изображение:").pack(pady=10)
        self.prompt_entry = tk.Entry(root, width=50)
        self.prompt_entry.pack(pady=5)
        
        # Кнопка отправки
        self.generate_button = tk.Button(root, text="Отправить", command=self.generate_image)
        self.generate_button.pack(pady=10)
        
        # Статус
        self.status_label = tk.Label(root, text="")
        self.status_label.pack(pady=5)
    
    def generate_image(self):
        prompt = self.prompt_entry.get().strip()
        if not prompt:
            messagebox.showwarning("Предупреждение", "Введите описание изображения")
            return
        
        self.status_label.config(text="Генерация изображения...")
        self.generate_button.config(state="disabled")
        
        # Запуск в отдельном потоке
        thread = threading.Thread(target=self.async_generate, args=(prompt,))
        thread.daemon = True
        thread.start()
    
    def async_generate(self, prompt):
        try:
            # Запуск асинхронной функции
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            image_url = loop.run_until_complete(self.generate_ai_image(prompt))
            loop.close()
            
            if image_url:
                self.root.after(0, lambda: self.show_image(image_url))
            else:
                self.root.after(0, lambda: self.show_error("Не удалось сгенерировать изображение"))
        except Exception as e:
            self.root.after(0, lambda: self.show_error(f"Ошибка: {str(e)}"))
    
    async def generate_ai_image(self, prompt):
        try:
            client = AsyncClient()
            response = await client.images.generate(
                prompt=prompt,
                model="flux",
                response_format="url"
            )
            return response.data[0].url
        except Exception as e:
            print(f"Ошибка генерации: {e}")
            return None
    
    def show_image(self, image_url):
        try:
            # Загрузка изображения
            response = requests.get(image_url)
            response.raise_for_status()
            
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            img.thumbnail((800, 600))
            photo = ImageTk.PhotoImage(img)
            
            # Открытие нового окна
            image_window = Toplevel(self.root)
            image_window.title("Сгенерированное изображение")
            
            label = tk.Label(image_window, image=photo)
            label.image = photo  # Сохраняем ссылку
            label.pack(padx=10, pady=10)
            
            self.status_label.config(text="Изображение сгенерировано!")
            
        except Exception as e:
            self.show_error(f"Ошибка загрузки изображения: {str(e)}")
        
        finally:
            self.generate_button.config(state="normal")
    
    def show_error(self, message):
        messagebox.showerror("Ошибка", message)
        self.status_label.config(text="")
        self.generate_button.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = AIImageGenerator(root)
    root.mainloop()
    