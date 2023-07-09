"""
3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""
OUT_OF_RANGE = 0
MIN_DIVIDEND = 2
MAX_ALLOWED = 100000
ONE_EXCEPTION = 1

num = int(input('Введите число: '))
if num <= OUT_OF_RANGE:
    print('Введено не положительное число')
elif num > MAX_ALLOWED:
    print('Введено недопустимо большое значение')
elif num == ONE_EXCEPTION:
    print('1 - составное число')
else:
    is_simple = True
    for i in range(MIN_DIVIDEND, num):
        if num % i == 0:
            is_simple = False
    if is_simple:
        print(f'{num} - простое число')
    else:
        print(f'{num} - составное число')