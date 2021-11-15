#!/usr/bin/python3

import numpy as np


class Matrix:

    def __init__(self, m, n):
        self.row = m
        self.column = n
        self.matrix1 = np.zeros((self.row, self.column), dtype=int)

    def __str__(self):
        return str(self.matrix1)

    def get(self, a, b):
        if a not in range(self.row+1):
            print('El valor deseado no pertenece a la matriz.')
        elif b not in range(self.column+1):
            print('El valor deseado no pertenece a la matriz.')
        else:
            print(
                'El valor ubicado en la fila {} '
                'y en la columna {} es: {}'
                .format(a, b, self.matrix1[a - 1][b - 1]))

    def set(self, value, a, b):
        if a not in range(self.row+1):
            print('El valor deseado no pertenece a la matriz.')
        elif b not in range(self.column+1):
            print('El valor deseado no pertenece a la matriz.')
        else:
            self.matrix1[a-1][b-1] = value
            return self.matrix1

    def __add__(self, other):
        if np.shape(self.matrix1) != np.shape(other.matrix1):
            print('Las matrices no se pueden sumar')
        else:
            sum = self.matrix1 + other.matrix1
            return sum

    def __sub__(self, other):
        if np.shape(self.matrix1) != np.shape(other.matrix1):
            print('Las matrices no se pueden restar')
        else:
            sub = self.matrix1 - other.matrix1
            return sub
