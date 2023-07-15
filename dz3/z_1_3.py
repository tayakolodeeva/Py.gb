"""
1. Решить задачи, которые не успели решить на семинаре.

Задание №8
Погружение в Python | Коллекции
✔ Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей.
"""
friends_list = {
    'Александр': ('палатка', 'фонарик', 'вода', 'сухое топливо'),
    'Михаил': ('палатка', 'спальный мешок', 'сухое топливо', 'вода'),
    'Максим': ('палатка', 'котелок', 'сухое топливо', 'удочка'),
    'Артём': ('палатка', 'спальный мешок', 'вода', 'коврик', 'аккумулятор'),
    'Лев': ('палатка', 'спальный мешок', 'вода', 'коврик', 'аккумулятор','фонарик'),
    'Иван': ('палатка', 'спальный мешок', 'вода', 'коврик', 'аккумулятор',  'удочка')
}

common_items = set(friends_list[list(friends_list.keys())[0]])
for key, value in friends_list.items():
    common_items = common_items.intersection(value)
print(common_items,'есть у всех друзей')

qty_items = dict()
for value in friends_list.values():
    for item in value:
        item_val = qty_items.setdefault(item, 0)
        qty_items[item] += 1
unique_items = []
for key, value in qty_items.items():
    if value == 1:
        unique_items.append(key)
print(unique_items, 'взял только один друг')

absent_items = []
absent_friends = dict()
for key, value in qty_items.items():
    if value == (len(friends_list) - 1):
        absent_items.append(key)
for item in absent_items:
    for key,value in friends_list.items():
        if item not in value:
            absent_friends[key] = item
print(absent_friends, 'то что только он не взял')


