import random

def is_valid(n, s):
    if n.isdigit() and 1 <= int(n) <= s:
        return True
    else:
        return False
    

max_dig = int(input('Введите максимальное число: '))
n = random.randint(1, max_dig)
print('Добро пожаловать в числовую угадайку', n)
count = 0
while True:
    print(f'Введите число от 1 до {max_dig}')
    m = input()
    if not is_valid(m, max_dig):
        print(f'А может быть все-таки введем целое число от 1 до {max_dig}?')
        continue
    m = int(m)
    if m < n:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        count += 1
    if m > n:
        print('Ваше число больше загаданного, попробуйте еще разок')
        count += 1
    if n == m:
        print(f'Вы угадали, поздравляем! Колличество попыток: {count+1}')
        print('Хочешь сыграть еще раз? Да/Нет')
        while True:
            answer = input().capitalize()
            if answer == 'Да':
                max_dig = int(input('Введите максимальное число: '))
                n = random.randint(1, max_dig)
                print('Добро пожаловать в числовую угадайку', n)
                count = 0
                break
            elif answer == 'Нет':
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                exit()
            else:
                print('Введите Да/Нет')

