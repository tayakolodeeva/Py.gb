"""
Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
Создайте класс Матрица. Добавьте методы для: - вывода на печать,
сравнения,
сложения,
*умножения матриц
"""
class Matrix:
    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def __new__(cls, matrix: list[list[int]]):
        if type(matrix) is list and len({len(row) for row in matrix}) == 1:
            return super().__new__(cls)
        else:
            print('Matrix argument is not valid!')
            return None

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
            print('Matrix cannot be added')
            return None

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
            print('Matrix cannot be multiplied')
            return None

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
    matrix_1 = Matrix([[1, 22, 33, 444], [55, 666, 77, 88]])
    matrix_2 = Matrix([[444, 33, 1, 22], [666, 55, 88, 77]])
    print(repr(matrix_1))

    print(matrix_1 == matrix_2)
    print(matrix_1 > matrix_2)

    matrix_4 = matrix_1 + matrix_2
    print(matrix_4)

    matrix_3 = Matrix([[40, 25], [60, 3], [100, 1], [55, 55]])
    matrix_5 = matrix_1 * matrix_3
    print(matrix_5)