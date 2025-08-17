import time

pas = input('Введите пароль длиной 8 символов: ')

while len(pas) < 8 or ' ' in pas:
    if ' ' in pas:
        pas = input('Пароль не должен содержать пробелы: ')
    else:
        pas = input('Длина меньше 8 символов, введите пароль повторно: ')
print('Пароль принят!')

time.sleep(2)