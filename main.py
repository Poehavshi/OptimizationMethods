from functions import f1, f2, f3, f4

NUMBER_OF_DASHES = 40
EPSILON = 0.0025
PRECISION = 0.005
N = 20


def find_min_by_dichotomy(a, b, f, epsilon, precision, not_an_argument):
    if epsilon > precision:
        raise ValueError("epsilon must be < precision")
    count = 0
    while abs(a - b) > precision:
        x = (a + b) / 2
        y1 = f(x - epsilon / 2)
        y2 = f(x + epsilon / 2)
        if y1 <= y2:
            b = x + epsilon / 2
        elif y1 > y2:
            a = x - epsilon / 2
        count += 1
    print(f"Count number: {count}")
    return x


def find_min_by_gold(a, b, f, not_an_argument, epsilon, not_an_argument_2):
    count = 0
    y1 = f(abs(a - b) * 0.382 + a)
    y2 = f(b - abs(a - b) * 0.382)
    while abs(b - a) > epsilon:
        count += 1
        if y1 < y2:
            b -= abs(a - b) * 0.382
            y2 = y1
            y1 = f(abs(a - b) * 0.382 + a)
        else:
            a += abs(a - b) * 0.382
            y1 = y2
            y2 = f(b - abs(a - b) * 0.382)

    x = (a + b) / 2
    print(f"Count number: {count}")
    return x


def find_min_by_fibonachi(a, b, f, not_an_argument, not_an_argument_2, n):
    count = 0
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


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def print_examples(find_min_method):
    print("-" * NUMBER_OF_DASHES + find_min_method.__name__ + "-" * NUMBER_OF_DASHES)
    print("1 function:", find_min_method(-10, 10, f1, EPSILON, PRECISION, N), "\n")
    print("2 function:", find_min_method(-2, 3, f2, EPSILON, PRECISION, N), "\n")
    print("3 function:", find_min_method(-2, 2, f3, EPSILON, PRECISION, N), "\n")
    print("4 function:", find_min_method(-10, 10, f4, EPSILON, PRECISION, N))


if __name__ == '__main__':
    print_examples(find_min_by_dichotomy)
    print_examples(find_min_by_gold)
    print_examples(find_min_by_fibonachi)
