text = input("Введите текст: ")

vowel = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"

# Создаем список гласных букв из текста
vowels = [char for char in text if char in vowel]

print("Список гласных букв:", vowels)
print("Длина списка:", len(vowels))