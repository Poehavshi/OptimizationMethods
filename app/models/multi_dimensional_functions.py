from abc import ABC

import numpy as np

from math import sqrt, cos, sin, cosh, sinh, pi

alpha = pi / 6


class AbstractFunction(ABC):
    def __init__(self, x0, y0):
        self.x0 = x0
        self.y0 = y0

    def __call__(self, *x):
        pass

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


class HyperbolicCosineFunction(AbstractFunction):
    def __init__(self, x0=1, y0=2):
        super(HyperbolicCosineFunction, self).__init__(x0, y0)

    def __call__(self, *coords):
        x_new = self.__calculate_x_new(coords)
        return np.array([[sinh(x_new[0]) * cos(alpha)], [sinh(x_new[1]) * sin(alpha)]])

    def grad(self, coords):
        x_new = self.__calculate_x_new(coords)
        return np.array([[sinh(x_new[0]) * cos(alpha)], [sinh(x_new[1]) * sin(alpha)]])

    def h(self, coords):
        x_new = self.__calculate_x_new(coords)
        return np.array([[cosh(x_new[0]) * cos(alpha) ** 2, 0.], [0., cosh(coords[1]) * sin(alpha) ** 2]])

    def __calculate_x_new(self, coords):
        coords = np.array(coords)
        x0 = self.x0
        y0 = self.y0
        return np.matrix([[(coords[0, 0] - x0) * cos(alpha) + (coords[1, 0] - y0) * sin(alpha)],
                          [(coords[1, 0] - y0) * sin(alpha) - (coords[0, 0] - x0) * cos(alpha)]], float)

    def __repr__(self):
        # !FIXME
        return f"Hyperbolic"


def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))
