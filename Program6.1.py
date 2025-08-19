import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def main():
    # Создаем главное окно и сразу скрываем его
    root = tk.Tk()
    root.withdraw()  # Скрываем основное окно
    
    try:
        # Показываем диалог выбора папки
        selected_folder = filedialog.askdirectory(
            title="Выберите папку с файлами .doc и .docx"
        )
        
        # Если пользователь отменил выбор
        if not selected_folder:
            print("Операция отменена пользователем.")
            return
        
        # Проверяем, что папка существует
        if not os.path.exists(selected_folder):
            messagebox.showerror("Ошибка", "Выбранная папка не существует!")
            return
        
        # Создаем путь для новой папки
        base_name = os.path.basename(selected_folder)
        parent_dir = os.path.dirname(selected_folder)
        new_folder_name = f"{base_name}_new"
        new_folder_path = os.path.join(parent_dir, new_folder_name)
        
        # Создаем новую папку, если она еще не существует
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
            print(f"Создана новая папка: {new_folder_path}")
        else:
            print(f"Папка уже существует: {new_folder_path}")
        
        # Получаем список файлов в исходной папке
        files = os.listdir(selected_folder)
        
        # Фильтруем только .doc и .docx файлы
        doc_files = [f for f in files if f.lower().endswith(('.doc', '.docx'))]
        
        if not doc_files:
            print("В выбранной папке не найдено файлов .doc или .docx")
            messagebox.showinfo("Информация", "В выбранной папке не найдено файлов .doc или .docx")
            return
        
        print(f"Найдено {len(doc_files)} файлов для перемещения:")
        
        # Перемещаем файлы
        moved_count = 0
        for filename in doc_files:
            source_path = os.path.join(selected_folder, filename)
            destination_path = os.path.join(new_folder_path, filename)
            
            try:
                shutil.move(source_path, destination_path)
                print(f"✓ Перемещен: {filename}")
                moved_count += 1
            except Exception as e:
                print(f"✗ Ошибка при перемещении {filename}: {e}")
        
        # Выводим итоговую информацию
        print(f"\nОперация завершена успешно!")
        print(f"Перемещено файлов: {moved_count}/{len(doc_files)}")
        print(f"Исходная папка: {selected_folder}")
        print(f"Новая папка: {new_folder_path}")
        
        # Показываем информационное сообщение
        messagebox.showinfo(
            "Успех", 
            f"Операция завершена!\nПеремещено файлов: {moved_count}/{len(doc_files)}\n"
            f"Новая папка: {new_folder_path}"
        )
        
    except Exception as e:
        error_msg = f"Произошла ошибка: {str(e)}"
        print(error_msg)
        messagebox.showerror("Ошибка", error_msg)

if __name__ == "__main__":
    main()