import hydra
from omegaconf import DictConfig
import logging

from app.models.functions_of_one_argument import f1, f2, f3, f4, fib
from types import FunctionType
from collections import namedtuple

log = logging.getLogger(__name__)


def find_min_by_dichotomy(a: float, b: float, f: FunctionType, **kwargs) -> float:
    """
    Function to find min by dichotomy method, also known as bisection method.
    The method consists of repeatedly bisecting the interval defined by
    these values and then selecting the sub interval in which the function changes sign,
    and therefore must contain a root.
    https://en.wikipedia.org/wiki/Bisection_method

    :param a: start of the interval
    :param b: end of the interval
    :param f: function to find min on that interval
    :keyword precision - precision of answer
    :keyword epsilon - size of epsilon-locality
    :return: x of function minimum
    """
    epsilon = kwargs["epsilon"]
    precision = kwargs["precision"]
    if epsilon > precision:
        raise ValueError("epsilon must be < precision")
    if a > b:
        raise ValueError("a must be < b")
    count = 0
    x = None
    while abs(a - b) > precision:
        x = (a + b) / 2
        y1 = f(x - epsilon / 2)
        y2 = f(x + epsilon / 2)
        if y1 <= y2:
            b = x + epsilon / 2
        elif y1 > y2:
            a = x - epsilon / 2
        count += 2
    log.info(f"Iterations: {count}")
    return x


def find_min_by_gold(a: float, b: float, f: FunctionType, **kwargs) -> float:
    """
    Function to find min by golden-section search method.
    For a strictly unimodal function with an extremum inside the interval, it will find that extremum,
    while for an interval containing multiple extrema (possibly including the interval boundaries),
    it will converge to one of them. If the only extremum on the interval is on a boundary of the interval,
    it will converge to that boundary point.
    https://en.wikipedia.org/wiki/Golden-section_search

    :param a: start of the interval
    :param b: end of the interval
    :param f: function to find min on that interval
    :keyword precision - precision of answer
    :return: x of function minimum
    """
    precision = kwargs["precision"]
    if a > b:
        raise ValueError("a must be < b")
    y1 = f((b - a) * 0.382 + a)
    y2 = f(b - (b - a) * 0.382)
    count = 2
    while b - a > precision:
        count += 1
        if y1 < y2:
            b -= (b - a) * 0.382
            y2 = y1
            y1 = f((b - a) * 0.382 + a)
        else:
            a += (b - a) * 0.382
            y1 = y2
            y2 = f(b - (b - a) * 0.382)

    x = (a + b) / 2
    log.info(f"Count number: {count}")
    return x


def find_min_by_fibonacci(a: float, b: float, f: FunctionType, **kwargs) -> float:
    """
    Function to find min by fibonacci search method.
    A very similar to golden ratio method.
    In order to approximate the probe positions of golden section search while probing only integer sequence indices,
    the variant of the algorithm for this case typically maintains a bracketing of the solution in which the length of
    the bracketed interval is a Fibonacci number.
    For this reason, the sequence variant of golden section search is often called Fibonacci search.
    https://en.wikipedia.org/wiki/Fibonacci_search_technique

    :param a: start of the interval
    :param b: end of the interval
    :param f: function to find min on that interval
    :keyword n - number of maximum fibonacci argument
    :return: x of function minimum
    """
    n = kwargs["n"]
    if a > b:
        raise ValueError("a must be < b")
    count = 2
    x1 = a + (b - a) * fib(n - 2) / fib(n)
    x2 = a + (b - a) * fib(n - 1) / fib(n)
    y1 = f(x1)
    y2 = f(x2)
    while n != 3:
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
    log.info(f"Count number: {count}")
    return x


def print_examples(find_min_method, config: DictConfig):
    """
    log.info examples of methods usage

    :param config: config from hydra
    :param find_min_method: method to find min
    """
    log.info("-" * config.dashes_number + find_min_method.__name__ + "-" * config.dashes_number)
    case = namedtuple('TestCase', ['a', 'b', 'f'])
    #                  a    b   f
    test_cases = (case(-10, 10, f1),
                  case(-2, 3, f2),
                  case(-2, 2, f3),
                  case(-10, 10, f4))

    for i, case in enumerate(test_cases):
        log.info(case.f.__doc__)
        log.info(f"min x = {find_min_method(*case, epsilon=config.epsilon, precision=config.precision, n=config.N)} \n")


@hydra.main(config_path="./conf", config_name="1d_methods")
def main(config: DictConfig):
    print_examples(find_min_by_dichotomy, config)
    print_examples(find_min_by_gold, config)
    print_examples(find_min_by_fibonacci, config)


if __name__ == '__main__':
    main()
