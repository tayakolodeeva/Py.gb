"""
Напишите функцию для транспонирования матрицы
"""
def transporation(table):
    table2 = []

    for i in range(len(table[0])):
        table2.append(list())
        for j in range(len(table)):
            table2[i].append(table[j][i])
    return table2

matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix)
matrix2 = transporation(matrix)
print(matrix2)