"""
2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента. 
Если ключ не хешируем, используйте его строковое представление.
"""

def hashable_dicts(**kwargs):
    reverse_dict = dict()
    for key, value in kwargs.items():
        if isinstance(value, (list, dict, set)):
            value = str(value)
        reverse_dict[value] = key
    return reverse_dict


print(hashable_dicts(students=["Александр", "Михаил"], \
                     three_frends={1: "Максим", 2: "Артём", 3: "Лев"}))