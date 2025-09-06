s = 'Число\tКвадрат'

print(f"{s}\n\n{'=' * len(s)}\n")

for i in range(1, 11):
    print(f"    {i}     {i**2}\n")

input('Нажмите Enter чтобы закрыть программу.')