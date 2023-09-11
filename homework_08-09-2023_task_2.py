'''
Задача № 2: Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
'''

import os

def split_file_path(file_path):
    # Сепарация html строки
    directory, filename = os.path.split(file_path)
    file_name, file_extension = os.path.splitext(filename)

    return directory, file_name, file_extension

# Проверка функции
file_path = "/path/to/your/file/filename.txt"
path, name, extension = split_file_path(file_path)

print("Путь к файлу:", path)
print("Имя файла:", name)
print("Расширение файла:", extension)
