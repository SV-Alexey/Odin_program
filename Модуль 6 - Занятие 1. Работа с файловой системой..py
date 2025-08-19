from tkinter import *
from tkinter import filedialog as fd
import os
import shutil


window = Tk()
window.withdraw()

direct = fd.askdirectory(title = "Выберите папку c документами .doc, .docx")

if direct:
    new_dir = direct + "_new"
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    else:
        print(f"Папка {new_dir} уже существует.")
    for file in os.listdir(direct):
        if file.lower().endswith((".doc", ".docx")):
            source_file = os.path.join(direct, file)
            destination_file = os.path.join(new_dir, file)
            try:
                shutil.move(source_file, destination_file)
                print(f"Файл {file} перемещен в {new_dir}")
            except Exception as e:
                print(f"Ошибка при перемещении файла {file}: {e}")
    print("Операция успешно завершена.") 
else:
    print("Папка не была выбрана.")

window.mainloop()
