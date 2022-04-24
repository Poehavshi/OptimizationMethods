from dataclasses import dataclass
from math import cosh, exp, tanh
from types import FunctionType


def f1(x: float) -> float:
    """f(x) = 10 - 1 / cosh((x - 3) ** 2)"""
    return 10 - 1 / cosh((x - 3) ** 2)


def f2(x: float) -> float:
    """f(x) = 1 / (1 + exp(-5 * x ** 2 + 10 * x))"""
    return 1 / (1 + exp(-5 * x ** 2 + 10 * x))


def f3(x: float) -> float:
    """f(x) = tanh(x ** 4 - 2 * x)"""
    return tanh(x ** 4 - 2 * x)


def f4(x: float) -> float:
    """f(x) = -1 / (1 + x ** 6)"""
    return -1 / (1 + x ** 6)


def fib(n: int) -> int:
    """
    Returns the fibonacci number of order n

    :param n: order number of Fibonacci number
    :return: fibonacci number of order n

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(3)
    2
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


@dataclass
class TestCase:
    a: int
    b: int
    f: FunctionType

