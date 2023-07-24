"""
3.Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите
код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг
друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара
бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от
1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если
бьют - ложь.

4.Напишите функцию в шахматный модуль. Используйте генератор случайных чисел
для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные
варианты и выведите 4 успешных расстановки.
"""
import random

__all__ = ['check_queens', 'check_queens_fast',
           'generate_coords', 'generate_coords_fast',
           'find_success_coords', 'find_success_coords_fast',
           'print_queens_board']

BOARD_SIZE = 8
QUEENS_QTY = 8


def check_queens(coords: set[tuple[int, int]]) -> bool:
    coords_list = list(coords)
    for i in range(len(coords_list) - 1):
        for j in range(i + 1, len(coords_list)):
            if coords_list[i][0] == coords_list[j][0] or coords_list[i][1] == coords_list[j][1]:
                return False
            if coords_list[i][0] + coords_list[i][1] == coords_list[j][0] + coords_list[j][1]:
                return False
            if coords_list[i][0] - coords_list[i][1] == coords_list[j][0] - coords_list[j][1]:
                return False

    return True


def check_queens_fast(coords: list[tuple[int, int]]) -> bool:
    for i in range(len(coords) - 1):
        for j in range(i + 1, len(coords)):
            if coords[i][0] + coords[i][1] == coords[j][0] + coords[j][1]:
                return False
            if coords[i][0] - coords[i][1] == coords[j][0] - coords[j][1]:
                return False

    return True


def generate_coords(queens_qty: int) -> set[tuple[int, int]]:
    queens_coords = set()
    while len(queens_coords) < queens_qty:
        queens_coords.add((random.randint(1, BOARD_SIZE), random.randint(1, BOARD_SIZE)))
    return queens_coords


def generate_coords_fast(queens_qty: int) -> list[tuple[int, int]]:
    queens_coords = []
    rows = [row for row in range(1, BOARD_SIZE + 1)]
    cols = [col for col in range(1, BOARD_SIZE + 1)]
    for _ in range(queens_qty):
        row = random.choice(rows)
        rows.remove(row)
        col = random.choice(cols)
        cols.remove(col)
        queens_coords.append((row, col))
    return queens_coords


def find_success_coords(queens_qty: int, coords_qty: int = 1) -> list[set[tuple[int, int]]]:
    safe_coords = []
    while len(safe_coords) < coords_qty:
        coords = generate_coords(queens_qty)
        if check_queens(coords) and coords not in safe_coords:
            safe_coords.append(coords)
    return safe_coords


def find_success_coords_fast(queens_qty: int, coords_qty: int = 1) -> list[set[tuple[int, int]]]:
    safe_coords = []
    while len(safe_coords) < coords_qty:
        coords = generate_coords_fast(queens_qty)
        if check_queens_fast(coords) and set(coords) not in safe_coords:
            safe_coords.append(set(coords))
    return safe_coords


def print_queens_board(coords: set[tuple[int, int]]):
    board = [['◻' if (i + j) % 2 == 0 else '◼' for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]
    for coord in coords:
        board[coord[0] - 1][coord[1] - 1] = '♛'
    for row in board:
        print(*row, sep=' ')

if __name__ == '__main__':
    success_coords_qty = 4

    for success_coord in find_success_coords_fast(QUEENS_QTY, success_coords_qty):
        print(f'\nКоординаты: {success_coord}')
        print_queens_board(success_coord)