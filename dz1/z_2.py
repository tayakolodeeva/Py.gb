"""
2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
Дано a, b, c - стороны предполагаемого треугольника. 
Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""
a = int(input('Введите длину стороны A: '))
b = int(input('Введите длину стороны B: '))
c = int(input('Введите длину стороны C: '))

if a <= 0 or b <= 0 or c <= 0:
    print('Длины сторон треугольника не могут быть отрицательными')
elif a < (b + c) and b < (a + c) and c < (a + b):
    if a == b or b == c or a == c:
        if a == b and b == c:
            print('Равносторонний треугольник')
        else:
            print('Равнобедренный треугольник')
    else:
        print('Разносторонний треугольник')
else:
    print('Треугольник не существует')