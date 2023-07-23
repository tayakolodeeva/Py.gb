"""
2. Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""

abs_path = r'C:\Users\Тая\Desktop\Py.o.dz.gb\dz5.txt'


def split_path(abs_path: str) -> tuple():
    list_abs_path = abs_path.split('\\')
    list_last_elem = list_abs_path[-1].split('.')
    path = '\\'.join(list_abs_path[0:-1])
    name = list_last_elem[0]
    expansion = list_last_elem[1]
    return path, name, expansion


print(split_path(abs_path))