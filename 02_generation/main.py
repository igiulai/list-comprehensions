n = int(input("Введите длину списка: "))
result = [1 if i % 2 == 0 else x % 5 for i, x in enumerate(range(n))]
print("Результат:", result)