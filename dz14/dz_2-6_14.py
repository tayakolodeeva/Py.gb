"""
2.Возьмите 1-3 задания из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним тесты.
3.2-5 тестов на задание в трёх вариантах:
4.doctest,
5.unittest,
6.pytest.

Task1

import doctest


def if_leap(year: int):
    return not (year % 4 != 0 or year % 100 == 0 and year % 400 != 0)


def check_date(str_date: str) -> bool:
    
    Checks if input string date is valid
    >>> check_date('01.01.2000')
    True
    >>> check_date('29.02.2000')
    True
    >>> check_date('29.02.2001')
    False
    >>> check_date('40.01.2000')
    False
    >>> check_date('31.04.2000')
    False
    >>> check_date('31.05.2000')
    True
    >>> check_date('10.13.2000')
    False

    day, month, year = map(int, str_date.split('.'))
    if not (1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 9999):
        return False

    if month in (4, 6, 9, 11) and day > 30:
        return False

    if month == 2 and if_leap(year) and day > 29:
        return False

    if month == 2 and not if_leap(year) and day > 28:
        return False

    return True


if __name__ == '__main__':
    doctest.testmod(verbose=True)

Task2
"""
import pytest


class QuadraticEquation:
    def __init__(self, a: float = 0, b: float = 0, c: float = 0):
        self.a = a
        self.b = b
        self.c = c
        self.d = self.get_d()

    def get_d(self) -> float:
        return self.b ** 2 - 4 * self.a * self.c

    def get_roots(self) -> float | tuple[float, float] | None:
        if self.d == 0:
            return -self.b / (2 * self.a)
        elif self.d > 0:
            return (-self.b + self.d ** 0.5) / (2 * self.a), (-self.b - self.d ** 0.5) / (2 * self.a)
        else:
            return None

    def __str__(self):
        res_str = ''
        if self.a:
            res_str += f'{self.a}x²'
        if self.b:
            res_str += f' + {self.b}x' if self.b > 0 else f' - {abs(self.b)}x'
        if self.c:
            res_str += ' + ' if self.c > 0 else ' - '
            res_str += str(abs(self.c))
        res_str += ' = 0'
        return res_str


def test_print():
    assert str(QuadraticEquation(4, 2, -3)) == f'4x² + 2x - 3 = 0'


def test_one_root():
    qe = QuadraticEquation(1, -4, 4)
    assert qe.get_roots() == 2


def test_two_roots():
    qe = QuadraticEquation(1, 3, -4)
    assert qe.get_roots() == (-4, 1) or qe.get_roots() == (1, -4)


def test_no_roots():
    qe = QuadraticEquation(1, -5, 9)
    assert qe.get_roots() is None


if __name__ == '__main__':
    pytest.main(['-vv'])