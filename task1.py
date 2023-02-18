# Напишите программу,
#  удаляющую из текста все слова, содержащие ""абв"".

text = input('Введите текст через пробел->')
print(f"Исходный текс : {text}")

findtext = 'абв'
my_list = [i for i in text.split() if findtext not in i]
print(f"Результат: {' '.join(my_list)}")