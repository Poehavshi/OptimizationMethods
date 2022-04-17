import logging
from types import FunctionType
import numpy as np

from omegaconf import DictConfig

log = logging.getLogger(__name__)


def __find_min_by_dichotomy(f: FunctionType, pos_0, pos_1, config: DictConfig):
    epsilon = config.epsilon
    max_iterations = config.N
    direction = ((pos_0 - pos_1) / np.linalg.norm(pos_0 - pos_1)) * epsilon
    i = 0
    for i in range(max_iterations):
        if np.linalg.norm(pos_1 - pos_0) < epsilon:
            break
        pos_c = (pos_1 + pos_0) * 0.5

        if f(*(pos_c+direction)) > f(*(pos_c-direction)):
            pos_1 = pos_c
            continue

        pos_0 = pos_c
    log.info(f"Dichotomy iterations number: {i}")
    return (pos_1+pos_0) * 0.5


def find_min_by_coordinate_descent(start_pos: tuple[float, float], f: FunctionType, config: DictConfig):
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

    opt_coord_n = 0
    step = 1

    pos_0 = np.array(start_pos)
    pos_1 = np.array(start_pos)

    for i in range(max_iterations):
        coordinate_number = i % len(start_pos)

        pos_1[coordinate_number] = pos_1[coordinate_number] - epsilon
        f_0 = f(*pos_1)

        pos_1[coordinate_number] = pos_1[coordinate_number] + 2 * epsilon
        f_1 = f(*pos_1)

        pos_1[coordinate_number] = pos_1[coordinate_number] + step if f_0 > f_1 else pos_1[coordinate_number] - step

        x_i = pos_0[coordinate_number]
        pos_1 = __find_min_by_dichotomy(f, pos_0, pos_1, config)

        pos_0 = pos_1

        if abs(pos_1[coordinate_number]-x_i) < epsilon:
            opt_coord_n += 1
            if opt_coord_n == len(pos_1):
                log.info(f"Per coord descend iterations number : {i}")
                return pos_0
            continue
        opt_coord_n = 0
    log.info(f"per coord descend iterations number : {max_iterations}")

    return pos_0
