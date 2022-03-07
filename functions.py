from math import cosh, exp, tanh


def f1(x):
    return 10 - 1 / cosh((x - 3) ** 2)


def f2(x):
    return 1 / (1 + exp(-5 * x ** 2 + 10 * x))


def f3(x):
    return tanh(x ** 4 - 2 * x)


def f4(x):
    return -1 / (1 + x ** 6)


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
