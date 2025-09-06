from tkinter import *
from tkinter import messagebox as mb


def book_seat(event=None):
    s = seat_entry.get()
    try:
        if seats[s] == 'свободно':
            seats[s] = 'забронировано'
            update_canvas()
            mb.showinfo("Успех", f"Место '{s}' успешно забронировано.")
            seat_entry.delete(0, END)
        else:
            mb.showinfo("Ошибка", f"Место '{s}' уже забронировано.")
            seat_entry.delete(0, END)
    except KeyError:
        mb.showinfo("Ошибка", f"Место '{s}' не существует.")
        seat_entry.delete(0, END)


def update_canvas():
    canvas.delete("all")
    for i, (seat, status) in enumerate(seats.items()):
        x = i * 40 + 20
        y = 20
        color = "green" if status == "свободно" else "red"
        canvas.create_rectangle(x, y, x+30, y+30, fill=color)
        canvas.create_text(x+15, y+15, text=seat)


def cancle_booking(event=None):
    s = cancle_seat_entry.get()
    try:
        if seats[s] == 'забронировано':
            seats[s] = 'свободно'
            update_canvas()
            mb.showinfo("Успех", f"Бронь места '{s}' успешно отменена.")
            cancle_seat_entry.delete(0, END)
        else:
            mb.showinfo("Ошибка", f"Место '{s}' не забронировано.")
            cancle_seat_entry.delete(0, END)
    except KeyError:
        mb.showinfo("Ошибка", f"Место '{s}' не существует.")
        cancle_seat_entry.delete(0, END)

window = Tk()
window.title("Бронирование мест")
window.geometry("400x400")

canvas = Canvas(width=400, height=60)
canvas.pack(pady=10)

legend_canvas = Canvas(width=300, height=50)
legend_canvas.pack(anchor='w')

legend_canvas.create_rectangle(10, 10, 40, 40, fill="green")
legend_canvas.create_text(50, 25, text="Свободно", anchor="w")

legend_canvas.create_rectangle(120, 10, 150, 40, fill="red")
legend_canvas.create_text(165, 25, text="Забронировано", anchor="w")

seats = {f"Б{i}": 'свободно' for i in range(1, 10)}
update_canvas()

seat_entry = Entry()
seat_entry.pack(pady=10)
seat_entry.focus()
seat_entry.bind("<Return>", book_seat)

Button(text="Забронировать место", command=book_seat).pack(pady=10)

cancle_seat_entry = Entry()
cancle_seat_entry.pack(pady=10)
cancle_seat_entry.bind("<Return>", cancle_booking)

Button(text="Отменить бронь", command=cancle_booking).pack(pady=10)

window.mainloop()