message = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))

lower_rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
upper_rus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
result = []

for char in message:
    if char in lower_rus:
        # Находим индекс и применяем сдвиг для строчных букв
        index = (lower_rus.index(char) + shift) % 33
        result.append(lower_rus[index])
    elif char in upper_rus:
        # Находим индекс и применяем сдвиг для заглавных букв
        index = (upper_rus.index(char) + shift) % 33
        result.append(upper_rus[index])
    else:
        # Оставляем символ как есть, если это не русская буква
        result.append(char)

print("Зашифрованное сообщение:", ''.join(result))