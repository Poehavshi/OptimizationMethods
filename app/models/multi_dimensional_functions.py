from abc import ABC, abstractmethod

import numpy as np

from math import sqrt, cos, sin, cosh, sinh, pi

alpha = pi / 6

A = 1
B = 2


class AbstractFunction(ABC):
    def __init__(self, x0, y0):
        self.x0 = x0
        self.y0 = y0

    @abstractmethod
    def __call__(self, *x):
        pass

    @abstractmethod
    def grad(self, coords):
        pass

    def h(self, coords):
        return np.array([[2., 0.], [0., 2.]])


class QuadraticFunction(AbstractFunction):
    def __init__(self, x0=sqrt(2), y0=-sqrt(3)):
        super(QuadraticFunction, self).__init__(x0, y0)

    def __call__(self, *coords):
        return (coords[0] - self.x0) ** 2 + (coords[1] - self.y0) ** 2

    def grad(self, coords):
        return np.array([[2 * (float(coords[0] - self.x0))], [2 * (float(coords[1] - self.y0))]])


class CosineFunction(AbstractFunction):
    def __init__(self, x0=1, y0=2):
        super(CosineFunction, self).__init__(x0, y0)

    def __call__(self, x: np.matrix):
        x_new = np.matrix(
            [[(x[0, 0] - self.x0) * cos(alpha) + (x[1, 0] - self.y0) * sin(alpha)],
             [(x[1, 0] - self.y0) * cos(alpha) - (x[0, 0] - self.x0) * sin(alpha)]],
            float)
        return A * (x_new[0]) ** 2 + B * (x_new[1]) ** 2

    def grad(self, x):
        x_new = np.matrix(
            [[2 * A * cos(alpha) * ((x[0, 0] - self.x0) * cos(alpha) + (x[1, 0] - self.y0) * sin(alpha)) -
              2 * B * sin(alpha) * ((x[1, 0] - self.y0) * cos(alpha) - (x[0, 0] - self.x0) * sin(alpha))],

             [2 * A * sin(alpha) * ((x[0, 0] - self.x0) * cos(alpha) + (x[1, 0] - self.y0) * sin(alpha))
              + 2 * B * cos(alpha) * ((x[1, 0] - self.y0) * cos(alpha) - (x[0, 0] - self.x0) * sin(alpha))]],
            float)

        return np.array([[x_new[0, 0]], [x_new[1, 0]]])

    # матрица Гессе
    def h(self, coords):
        return np.array([[2 * A * (cos(alpha)) ** 2 + 2 * B * (sin(alpha)) ** 2,
                          2 * (cos(alpha)) * (sin(alpha)) * (A - B)],
                         [2 * (cos(alpha)) * (sin(alpha)) * (A - B),
                          2 * A * (sin(alpha)) ** 2 + 2 * B * (cos(alpha)) ** 2]])

    def __calculate_x_new(self, coords):
        coords = np.array(coords)
        x0 = self.x0
        y0 = self.y0
        return np.matrix([[(coords[0, 0] - x0) * cos(alpha) + (coords[1, 0] - y0) * sin(alpha)],
                          [(coords[1, 0] - y0) * sin(alpha) - (coords[0, 0] - x0) * cos(alpha)]], float)

    def __repr__(self):
        return f"Cosine"
