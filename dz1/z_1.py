"""
1.Решить задачи, которые не успели решить на семинаре.
"""
# 8. Нарисовать в консоли ёлку спросив у пользователя количество рядов.
"""
rows = int(input('Введите количество рядов ёлки: '))
count = 1
step = " "
step2 = 1
star = "*" 
print(step)
while (rows > 0):
    three = step * (rows - count) + star * step2
    print(three)
    rows -= 1
    step2 += 2
"""
# 9.Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

for i in range(2, 11):
    for k in range(2, 6):
        print(k, 'X', i, '=', i * k, end='\t\t')
    print()

print()

for i in range(2, 11):
    for k in range(6, 10):
        print(k, 'X', i, '=', i * k, end='\t\t')
    print()