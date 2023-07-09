"""
2.Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""
HEX = 16
TEN16 = "A"
ELEVEN16 = "B"
TWELVE16 = "C"
THIRTEEN16 = "D"
FOURTEEN16 = "E"
FIFTEEN16 = "F"

number: int = int(input("Введите целое число: "))
temp: int = number
print(hex(number))

result: str = ""
while temp > 0:
    temp_result: int = temp % HEX
    match temp_result:
        case 10:
            result = TEN16 + result
        case 11:
            result = ELEVEN16 + result
        case 12:
            result = TWELVE16 + result
        case 13:
            result = THIRTEEN16 + result
        case 14:
            result = FOURTEEN16 + result
        case 15:
            result = FIFTEEN16 + result
        case _:
            result = str(temp_result) + result
    temp //= HEX
print(result)