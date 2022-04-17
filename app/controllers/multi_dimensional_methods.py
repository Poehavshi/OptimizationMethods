import logging
from types import FunctionType
from one_dimensional_methods import find_min_by_dichotomy

from omegaconf import DictConfig

log = logging.getLogger(__name__)


def find_min_by_coordinate_descent(start_pos: tuple[int], f: FunctionType, config: DictConfig):
    """
    Coordinate descent is an optimization algorithm that successively minimizes along coordinate directions to find
    the minimum of a function. At each iteration, the algorithm determines a coordinate or coordinate block via a
    coordinate selection rule, then exactly or inexactly minimizes over the corresponding coordinate hyperplane while
    fixing all other coordinates or coordinate blocks.

    https://en.wikipedia.org/wiki/Coordinate_descent
    :param start_pos: coordinates of start position
    :param config: hydra config with precisions parameters
    :param f: function to find min
    :return: x of function minimum
    """
    epsilon = config.epsilon
    max_iterations = config.N

    step = 1

    pos_0: list[int] = list(start_pos)
    pos_1: list[int] = list(start_pos)

    for i in range(max_iterations):
        coordinate_number = i % len(start_pos)

        pos_1[coordinate_number] = pos_1[coordinate_number] - epsilon
        f_0 = f(*pos_1)

        pos_1[coordinate_number] = pos_1[coordinate_number] + 2 * epsilon
        f_1 = f(*pos_1)

        pos_1[coordinate_number] = pos_1[coordinate_number] - epsilon
        pos_1[coordinate_number] = pos_1[coordinate_number] + step if f_0 > f_1 else pos_1[coordinate_number] - step

        x_i = pos_0[coordinate_number]
        x_1 = find_min_by_dichotomy()

    log.info(f"Count number: {max_iterations}")
    return pos_0
