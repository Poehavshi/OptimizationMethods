from functions import f1, f2, f3, f4, fib
from typing import Callable

NUMBER_OF_DASHES = 40
EPSILON = 0.0025
PRECISION = 0.005
N = 20


def find_min_by_dichotomy(a: float, b: float, f: Callable, **kwargs) -> float:
    epsilon = kwargs["epsilon"]
    precision = kwargs["precision"]
    if epsilon > precision:
        raise ValueError("epsilon must be < precision")
    if a > b:
        raise ValueError("a must be < b")
    count = 0
    while abs(a - b) > precision:
        x = (a + b) / 2
        y1 = f(x - epsilon / 2)
        y2 = f(x + epsilon / 2)
        if y1 <= y2:
            b = x + epsilon / 2
        elif y1 > y2:
            a = x - epsilon / 2
        count += 2
    print(f"Iterations: {count}")
    return x


def find_min_by_gold(a: float, b: float, f: Callable, **kwargs) -> float:
    precision = kwargs["precision"]
    if a > b:
        raise ValueError("a must be < b")
    count = 0
    y1 = f((b-a) * 0.382 + a)
    y2 = f(b - (b-a) * 0.382)
    while b - a > precision:
        count += 1
        if y1 < y2:
            b -= (b-a) * 0.382
            y2 = y1
            y1 = f((b-a) * 0.382 + a)
        else:
            a += (b-a) * 0.382
            y1 = y2
            y2 = f(b - (b-a) * 0.382)

    x = (a + b) / 2
    print(f"Count number: {count}")
    return x


def find_min_by_fibonacci(a: float, b: float, f: Callable, **kwargs) -> float:
    n = kwargs["n"]
    if a > b:
        raise ValueError("a must be < b")
    count = 1
    x1 = a + (b - a) * fib(n - 2) / fib(n)
    x2 = a + (b - a) * fib(n - 1) / fib(n)
    y1 = f(x1)
    y2 = f(x2)

    while n != 1:
        count += 1
        n -= 1
        if y1 > y2:
            a = x1
            x1 = x2
            x2 = b - (x1 - a)
            y1 = y2
            y2 = f(x2)
        else:
            b = x2
            x2 = x1
            x1 = a + (b - x2)
            y2 = y1
            y1 = f(x1)

    x = (x1 + x2) / 2

    print(f"Count number: {count}")
    return x


def print_examples(find_min_method):
    print("-" * NUMBER_OF_DASHES + find_min_method.__name__ + "-" * NUMBER_OF_DASHES)
    #              a    b   f
    test_cases = [[-10, 10, f1],
                  [-2,  3,  f2],
                  [-2,  2,  f3],
                  [-10, 10, f4]]
    for i, case in enumerate(test_cases):
        print(f"{i+1} function:", find_min_method(*case, epsilon=EPSILON, precision=PRECISION, n=N), "\n")


if __name__ == '__main__':
    print_examples(find_min_by_dichotomy)
    print_examples(find_min_by_gold)
    print_examples(find_min_by_fibonacci)
