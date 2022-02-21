from functions import f1, f2, f3, f4


def find_min_by_dichotomy(a, b, f, epsilon, precision):
    if epsilon > precision:
        raise ValueError("epsilon must be lesser than precision")
    count = 0
    while abs(a - b) > precision:
        x = (a + b) / 2
        f1_value = f(x - epsilon)
        f2_value = f(x + epsilon)
        if f1_value <= f2_value:
            b = x + epsilon / 2
        elif f1_value > f2_value:
            a = x - epsilon / 2
        count += 1
    print(count)
    return x


if __name__ == '__main__':
    print("First function:", find_min_by_dichotomy(-10, 10, f1, 0.25, 0.5))
    print("Second function:", find_min_by_dichotomy(-2, 3, f2, 0.25, 0.5))
    print("Third function:", find_min_by_dichotomy(-2, 2, f3, 0.25, 0.5))
    print("Fourth function:", find_min_by_dichotomy(-10, 10, f4, 0.25, 0.5))
