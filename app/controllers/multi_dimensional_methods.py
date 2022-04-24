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
    epsilon = np.array([[config['epsilon'], config['epsilon']]])
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
            print(f"Iterations: {iteration}")
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
    epsilon = np.array([[config['epsilon'], config['epsilon']]])
    iteration = 0
    while True:
        x_prev = np.copy(x)
        fx_prev = f(x_prev)
        grad_fx = f.grad(x)
        x -= step * grad_fx
        fx = f(x)
        while fx < fx_prev:
            x -= step * grad_fx
            fx_prev = fx
            fx = f(x)
            iteration += 1

        if all(np.abs(x - x_prev) < epsilon):
            print(f"Iterations: {iteration}")
            return x


def newton_descent(f: AbstractFunction, H, x, config: DictConfig):
    """
    Newton Descent
    :param f: function
    :param H: matrix of second derivatives of f
    :param x: starting points
    :param config: config with precision parameters
    :return: minimum of function
    :return: minimum of function
    """
    epsilon = np.array([[config['epsilon'], config['epsilon']]])
    iteration = 0
    while True:
        x_prev = np.copy(x)
        x = x - np.linalg.inv(H(x)).dot(f.grad(x))
        iteration += 1

        if all(np.abs(x - x_prev) < epsilon):
            print(f"Iterations: {iteration}")
            return x
