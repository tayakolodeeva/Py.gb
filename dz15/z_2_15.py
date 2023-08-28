"""
Возьмите любые 1-3 задания из прошлых домашних заданий. 
Добавьте к ним логирование ошибок и полезной информации. 
Также реализуйте возможность запуска из командной строки с передачей параметров. 

Task1

from typing import Callable
from functools import wraps
import logging

logging.basicConfig(filename='guess.log', filemode='a', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


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
            logger.error(f'Secret number {secret_num} is out of range ({min_number}, {max_number})')
            raise OutOfRangeException(secret_num, min_number, max_number)
        if not min_guess_trials <= guess_qty <= max_guess_trials:
            logger.error(f'Quantity of trials should be positive number: {guess_qty}')
            raise InvalidTrialsException(guess_qty)

        return func(secret_num, guess_qty, *args, **kwargs)

    return wrapper


def log_params(func: Callable) -> Callable[[list, dict], int]:
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f'args: {args}, result: {result}')
        return result

    return wrapper


@validate
@log_params
def guess_num(secret_num: int, guess_qty: int):
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
    guess_num(100, 2)

Task2    
"""
import argparse
import logging

LOG_FORMAT = '{levelname} - {asctime} - {msg}'

logging.basicConfig(filename='date_checker.log', filemode='a', encoding='utf-8', level=logging.INFO,
                    format=LOG_FORMAT, style='{')
logger = logging.getLogger(__name__)


def if_leap(year: int):
    return not (year % 4 != 0 or year % 100 == 0 and year % 400 != 0)


def check_date(str_date: str) -> bool:
    result = True

    try:
        day, month, year = map(int, str_date.split('.'))
    except ValueError as e:
        logger.error(f'Can\'t parse date sting! Error: {e}')
        raise ValueError(e)

    if not (1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 9999):
        result = False

    if month in (4, 6, 9, 11) and day > 30:
        result = False

    if month == 2 and if_leap(year) and day > 29:
        result = False

    if month == 2 and not if_leap(year) and day > 28:
        result = False

    logger.info(f'Date: {str_date} - {"" if result else "not "}valid')

    return result


def parse():
    parser = argparse.ArgumentParser(prog='check_date',
                                     description='Checks if input string date valid',
                                     epilog='Date example: 01.01.2000')
    parser.add_argument('-d', '--date', help='Date to check', type=str)
    args = parser.parse_args()
    return check_date(args.date)


if __name__ == '__main__':
    print(parse())