s = input("Введите строку: ")

first = s.index('h')
last = s.rindex('h')

result = s[:first+1] + s[first+1:last][::-1] + s[last:]
print("Результат:", result[first+1:last])