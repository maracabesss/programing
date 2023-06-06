import os

while True:

# Запитуємо шлях до файлу від користувача

file_path = input("Введіть шлях до файлу: ")

if not os.path.isfile(file_path):
    print("Файл не знайдено!")
    continue

# Відкриваємо файл і читаємо його вміст
with open(file_path, "r") as file:
    content = file.readlines()

# Ініціалізуємо змінні для збереження статистики
num_lines = len(content)
num_empty_lines = 0
num_z_lines = 0
num_z_chars = 0
num_and_lines = 0

# Обчислюємо статистику
for line in content:
    if line.strip() == "":
        num_empty_lines += 1
    if "z" in line:
        num_z_lines += 1
        num_z_chars += line.count("z")
    if "and" in line:
        num_and_lines += 1

# Виводимо статистику на екран
print(f"Кількість рядків: {num_lines}")
print(f"Кількість порожніх рядків: {num_empty_lines}")
print(f"Кількість рядків з літерою 'z': {num_z_lines}")
print(f"Кількість літер 'z' у файлі: {num_z_chars}")
print(f"Кількість рядків з групою символів 'and': {num_and_lines}")

# Запитуємо користувача, чи бажає він проаналізувати ще один файл
choice = input("Бажаєте проаналізувати ще один файл? (y/n): ")
if choice.lower() != "y":
    break
