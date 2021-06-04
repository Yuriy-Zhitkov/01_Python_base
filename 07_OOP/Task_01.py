'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
'''

import copy # для создания полной копии первой матрицы при переопределении метода __add__

class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        my_str = ''
        for el in self.matrix:
              my_str += str(el) + '\n'
        return my_str

    def __add__(self, other):
        result = copy.deepcopy(self.matrix)
        for line in range(len(result)):
            for col in range(len(result[line])):
                result[line][col] += other.matrix[line][col]
        return Matrix(result)


a = Matrix([[1,2,3], [4,5,6], [7,8,9]])
b = Matrix([[1,2,3], [4,5,6], [7,8,9]])
c = Matrix([[1,2,3], [4,5,6], [7,8,9]])

print(a)
print(a + b + c)




