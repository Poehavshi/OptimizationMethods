import logging
import numpy as np
from app.models.multi_dimensional_functions import AbstractFunction

from omegaconf import DictConfig

log = logging.getLogger(__name__)


def coordinate_descent(f: AbstractFunction, x, config: DictConfig):
    """
    Coordinate Descent
    :param f: function
    :param x: starting point
    :param config: config with precision parameters
    :return: minimum of function
    """
    step = config['step']
    eps = config['epsilon']
    epsilon = np.array([[eps],
                        [eps]])
    iteration = 0
    while True:
        x_prev = np.copy(x)
        for i in range(0, len(x)):
            x_new = np.copy(x)
            x_new[i] += step
            fx = f(x)
            fx_new = f(x_new)

            while fx_new < fx:
                x[i] = x_new[i]
                fx = fx_new
                x_new[i] += step
                fx_new = f(x_new)
                iteration += 1

        if all(np.abs(x - x_prev) < epsilon):
            log.info(f"Coordinate descent number of iterations: {iteration}")
            return x


def gradient_descent(f: AbstractFunction, x, config: DictConfig):
    """
    Gradient Descent
    :param x: starting point
    :param config: config with precision parameters
    :param f: function
    :return: minimum of function
    """
    step = config['step']
    eps = config['epsilon']
    epsilon = np.array([[eps],
                        [eps]])
    step, iteration = 0, 0
    i = 0
    mx = 100
    while True:
        step = 1 / min(i + 1, mx)
        i += 1
        x_prev = np.copy(x)
        fx_prev = f(x_prev)
        grad_fx = f.grad(x)
        x -= step * grad_fx
        fx = f(x)
        while fx < fx_prev:
            iteration += 1
            x -= step * grad_fx
            fx_prev = fx
            fx = f(x)

        if all(np.abs(x - x_prev) < epsilon):
            log.info("Gradient descent number of iterations: ", iteration)
            return x


def newton_descent(f: AbstractFunction, x, config: DictConfig):
    """
    Newton Descent
    :param f: function
    :param H: matrix of second derivatives of f
    :param x: starting points
    :param config: config with precision parameters
    :return: minimum of function
    :return: minimum of function
    """
    eps = config['epsilon']
    epsilon = np.array([[eps],
                        [eps]])
    iteration = 0
    while True:
        x_prev = np.copy(x)
        x = x - np.linalg.inv(f.h(x)).dot(f.grad(x))
        iteration += 1

        if all(np.abs(x - x_prev) < epsilon):
            log.info(f"Newton descent number of iterations: {iteration}")
            return x
