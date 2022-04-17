import numpy as np


def f1(*x) -> float:
    """
    Minimum at point:
    x1 = 2.5
    x2 = 1.5
    :param x: 2d tuple of coordinates
    :return: f(x1, x2) = (x1-5)*x1 + (x2-3)*x2
    """
    return (x[0] - 5) * x[0] + (x[1] - 3) * x[1]


def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))
