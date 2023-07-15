"""
2. Дан список повторяющихся элементов. 
Вернуть список с дублирующимися элементами. 
В результирующем списке не должно быть дубликатов.
"""
element_list = [4, 9, 5, 1, 6, 8, 8, 8, 4, 9, 8, 10, 9, 2, 10]
doubles = set()

for item in element_list:
    if element_list.count(item) > 1:
        doubles.add(item)

print('Список элементов:', element_list)
print('Повторяющиеся элементы:', list(doubles))