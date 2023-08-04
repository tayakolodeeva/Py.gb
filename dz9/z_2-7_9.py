"""
2.Напишите следующие функции:
3.Нахождение корней квадратного уравнения
4.Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
5.Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
6.Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
"""

import json
from functools import wraps
from random import randint, uniform
from typing import Callable
import csv


def gen_float_trios(file_path: str, min_rows: int = 100, max_row: int = 1000,
                    min_float: float = -100.0, max_float: float = 100) -> None:

    with open(file_path, 'w', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
        for _ in range(randint(min_rows, max_row)):
            csv_writer.writerow(uniform(min_float, max_float) for _ in range(3))


def add_params_from_csv(func: Callable[[float], float]) -> Callable[[str], list[dict]]:
    @wraps(func)
    def wrapper(csv_file_path: str) -> list[dict]:
        with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
            result = []
            for params in csv_reader:
                cur_result = {
                    'params': params,
                    'result': func(*params)
                }
                result.append(cur_result)
            return result

    return wrapper


def log2json(func: Callable) -> Callable[[list, dict], int]:
    @wraps(func)
    def wrapper(*args, **kwargs):
        file_path = f'{func.__name__}.json'
        result = func(*args, **kwargs)
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(result, json_file, indent=2, ensure_ascii=False)

        return result

    return wrapper


@log2json
@add_params_from_csv
def quadratic_equation(a: float, b: float, c: float) -> float | tuple[float | str, float | str]:
    d = b ** 2 - 4 * a * c
    if d == 0:
        return -b / (2 * a)
    elif d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    else:
        d = complex(d, 0)
        return str((-b + d ** 0.5) / (2 * a))[1:-1], str((-b - d ** 0.5) / (2 * a))[1:-1]


if __name__ == '__main__':
    gen_float_trios('number_trios.csv')
    quadratic_equation('number_trios.csv')