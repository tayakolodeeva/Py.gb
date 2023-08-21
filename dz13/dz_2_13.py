"""
2. Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. 
Напишите к ним классы исключения с выводом подробной информации. 
Поднимайте исключения внутри основного кода. 
Например нельзя создавать прямоугольник со сторонами отрицательной длины.

Task1

from typing import Type


class MatrixError(Exception):
    pass


class MatrixConsistencyError(MatrixError):
    def __init__(self, matrix: list[list]):
        self.matrix = matrix

    def __str__(self):
        return 'All incoming matrix rows should be the same length!'


class MatrixAdditionError(MatrixError):
    def __init__(self, self_rows: int, self_cols: int, other_rows: int, other_cols: int):
        self.self_rows = self_rows
        self.self_cols = self_cols
        self.other_rows = other_rows
        self.other_cols = other_cols

    def __str__(self):
        return f'Matrix cannot be added: Rows and columns of both matrix should be equal!\n' \
               f'Rows of matrixes are: {self.self_rows}, {self.other_rows}.\n' \
               f'Columns of matrixes are: {self.self_cols}, {self.other_cols}.'


class MatrixMultiplyError(MatrixError):
    def __init__(self, self_cols: int, other_rows: int):
        self.self_cols = self_cols
        self.other_rows = other_rows

    def __str__(self):
        return f'Matrix cannot be multiplied: ' \
               f'columns quantity of the first matrix ({self.self_cols}) ' \
               f'should be equal to rows quantity of the second matrix ({self.other_rows})!'


class Matrix:
    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def __new__(cls, matrix: list[list[int]]):
        if type(matrix) is not list:
            raise TypeError(f'Incoming matrix should be list. Current type: {type(matrix)}')

        if len({len(row) for row in matrix}) != 1:
            raise MatrixConsistencyError(matrix)

        return super().__new__(cls)

    def concat_rows(self):
        return [item for row in self.matrix for item in row]

    def __is_lengths_equal(self, other):
        return self.rows == other.rows and self.cols == other.cols

    def __eq__(self, other):
        if self.__is_lengths_equal(other):
            return sorted(self.concat_rows()) == sorted(other.concat_rows())
        return False

    def __lt__(self, other):
        if self.rows * self.cols < other.rows * other.cols:
            return True
        elif self.rows * self.cols > other.rows * other.cols:
            return False
        else:
            return sum(self.concat_rows()) < sum(other.concat_rows())

    def __le__(self, other):
        if self.rows * self.cols < other.rows * other.cols:
            return True
        elif self.rows * self.cols > other.rows * other.cols:
            return False
        else:
            return sum(self.concat_rows()) <= sum(other.concat_rows())

    def __add__(self, other):
        if self.__is_lengths_equal(other):
            sum_matrix = []
            for row_i in range(self.rows):
                sum_row = []
                for item_i in range(self.cols):
                    sum_row.append(self.matrix[row_i][item_i] + other.matrix[row_i][item_i])
                sum_matrix.append(sum_row)
            return Matrix(sum_matrix)
        else:
            raise MatrixAdditionError(self.rows, self.cols, other.rows, other.cols)

    def __mul__(self, other):
        if self.cols == other.rows:
            mul_matrix = []
            for row in self.matrix:
                mul_row = []
                for col_i in range(other.cols):
                    mul_row.append(sum(row[i] * other.matrix[i][col_i] for i in range(self.cols)))
                mul_matrix.append(mul_row)
            return Matrix(mul_matrix)
        else:
            raise MatrixMultiplyError(self.cols, other.rows)

    def __str__(self):
        max_length = max(map(lambda x: max(map(lambda y: len(str(y)), x)), self.matrix))
        output = ''
        for i in range(len(self.matrix)):
            output += '| '
            for j in range(len(self.matrix[i])):
                output += f'{self.matrix[i][j]:>{max_length}} '
            output += '|\n'
        return output

    def __repr__(self):
        return f'Matrix({self.matrix})'


if __name__ == '__main__':
    # matrix_1 = Matrix([[1, 22, 444], [55, 666, 77, 88]])
    matrix_1 = Matrix([[1, 22, 33, 444], [55, 666, 77, 88]])
    matrix_2 = Matrix('[444, 33, 1], [666, 55, 88]')
    matrix_2 = Matrix([[444, 33, 1], [666, 55, 88]])

    # matrix_4 = matrix_1 + matrix_2
    # matrix_5 = matrix_1 * matrix_2
"""
"""
Task2
"""
from typing import Callable
from functools import wraps
import random
from os.path import exists
import json


class GuessNumberException(Exception):
    pass


class OutOfRangeException(GuessNumberException):
    def __init__(self, number: int, min_num: int, max_num: int):
        self.number = number
        self.min_num = min_num
        self.max_num = max_num

    def __str__(self):
        return f'Secret number {self.number} is out of range ({self.min_num}, {self.max_num})'


class InvalidTrialsException(GuessNumberException):
    def __init__(self, trials_qty: int):
        self.trials_qty = trials_qty

    def __str__(self):
        return f'Quantity of trials should be positive number: {self.trials_qty}'


def validate(func: Callable) -> Callable[[int, int], None]:
    min_number = 1
    max_number = 100
    min_guess_trials = 1
    max_guess_trials = 10

    @wraps(func)
    def wrapper(secret_num: int, guess_qty: int, *args, **kwargs):
        if not min_number <= secret_num <= max_number:
            raise OutOfRangeException(secret_num, min_number, max_number)
        if not min_guess_trials <= guess_qty <= max_guess_trials:
            raise InvalidTrialsException(guess_qty)

        return func(secret_num, guess_qty, *args, **kwargs)

    return wrapper


def add_param_to_json(func: Callable) -> Callable[[list, dict], int]:
    @wraps(func)
    def wrapper(*args, **kwargs):
        file_path = f'{func.__name__}.json'
        data = []

        if exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)

        result = func(*args, **kwargs)
        cur_data = {
            'args': args,
            **kwargs,
            'result': result
        }
        data.append(cur_data)
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=2, ensure_ascii=False)

        return result

    return wrapper


def trials(calls_qty: int) -> Callable:
    results = []

    def deco(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(calls_qty):
                results.append(func(*args, **kwargs))
            return results

        return wrapper

    return deco


@trials(3)
@validate
@add_param_to_json
def guess_num(secret_num: int, guess_qty: int):
    """Guess number game"""
    for i in range(1, guess_qty + 1):
        answer = int(input(f'Номер попытки: {i}. Угадайте число от 1 до 100: '))
        if answer == secret_num:
            print('Вы угадали!')
            return
        elif answer > secret_num:
            print('Меньше')
        else:
            print('Больше')


if __name__ == '__main__':
    guess_num(100, 0)