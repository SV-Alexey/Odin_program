import tkinter as tk

root = tk.Tk()
root.title("Ф.И.О.")

# Первый фрейм - Имя
frame1 = tk.Frame(relief="ridge", bd=2)
frame1.pack(pady=10, padx=100)

tk.Label(frame1, text="Имя:").pack()
entry1 = tk.Entry(frame1)
entry1.pack(pady=5)
tk.Button(text="Ввести имя").pack()

# Второй фрейм - Фамилия
frame2 = tk.Frame(relief="ridge", bd=2)
frame2.pack(pady=10, padx=100)

tk.Label(frame2, text="Фамилия:").pack()
entry2 = tk.Entry(frame2)
entry2.pack(pady=5)
tk.Button(text="Ввести фамилию").pack()

# Третий фрейм - Отчество
frame3 = tk.Frame(relief="ridge", bd=2)
frame3.pack(pady=10, padx=100)

tk.Label(frame3, text="Отчество:").pack()
entry3 = tk.Entry(frame3)
entry3.pack(pady=5)
tk.Button(text="Ввести отчество").pack()

root.mainloop()
