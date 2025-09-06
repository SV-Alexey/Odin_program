with open('Demo.log') as file:
    content = file.read()

s1 = content.count("NEC")
s2 = content.count("SHARP")
s3 = content.count("SONY")

print(f'NEC = {s1}\nSHARP = {s2}\nSONY = {s3}')
input('Нажмите Enter, чтобы закрыть программу.')