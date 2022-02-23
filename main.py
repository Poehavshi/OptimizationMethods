from functions import f1, f2, f3, f4

NUMBER_OF_DASHES = 40


def find_min_by_dichotomy(start, end, f, epsilon, precision):
    if epsilon > precision:
        raise ValueError("epsilon must be lesser than precision")
    count = 0
    while abs(start - end) > precision:
        x = (start + end) / 2
        f1_value = f(x - epsilon)
        f2_value = f(x + epsilon)
        if f1_value <= f2_value:
            end = x + epsilon / 2
        elif f1_value > f2_value:
            start = x - epsilon / 2
        count += 1
    print(f"Count number: {count}")
    return x


def find_min_by_gold(a, b, f, epsilon, t):
    count = 2
    x1 = t * a + (1 - t) * b
    x2 = (1 - t) * a + t * b
    f1_value = f(x1)
    f2_value = f(x2)
    while abs(b - a) > epsilon:
        count += 1
        if f1_value < f2_value:
            b = x2
            if abs(b - a) > epsilon:
                x2 = x1
                f2_value = f1_value
                x1 = t * a + (1 - t) * b
                f1_value = f(x1)
        else:
            a = x1
            if abs(b - a) > epsilon:
                x1 = x2
                f1_value = f2_value
                x1 = (1 - t) * a + t * b
                f2_value = f(x1)
        x = (a + b) / 2
    print(f"Count number: {count}")
    return x


def print_test_examples(find_min_method):
    print("-" * NUMBER_OF_DASHES + "DICHOTOMY" + "-" * NUMBER_OF_DASHES)
    print("First function:", find_min_method(-10, 10, f1, 0.25, 0.5), "\n")
    print("Second function:", find_min_method(-2, 3, f2, 0.25, 0.5), "\n")
    print("Third function:", find_min_method(-2, 2, f3, 0.25, 0.5), "\n")
    print("Fourth function:", find_min_method(-10, 10, f4, 0.25, 0.5))


if __name__ == '__main__':
    print_test_examples(find_min_by_dichotomy)
    print_test_examples(find_min_by_gold)
