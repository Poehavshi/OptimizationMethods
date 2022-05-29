import logging

import hydra
import streamlit as st
from omegaconf import DictConfig

from app.models.multi_dimensional_functions import QuadraticFunction, CosineFunction, AbstractFunction
from app.controllers.multi_dimensional_methods import coordinate_descent, gradient_descent, newton_descent

import numpy as np
import matplotlib.pyplot as plt

log = logging.getLogger(__name__)


def two_argument_form(config: DictConfig):
    st.title("Functions of two and more arguments")
    methods = {'coordinate descent': coordinate_descent,
               'gradient descent': gradient_descent,
               'newton descent': newton_descent}

    method = methods[st.selectbox("Optimization method", methods)]

    # functions_to_optimize = {"quadratic": QuadraticFunction(), "hyperbolic": CosineFunction()}
    functions_to_optimize = {
        "Cosine (1, 2)": CosineFunction(),
        "Cosine (5, 1)": CosineFunction(5, 1)
    }
    function_to_optimize = functions_to_optimize[st.selectbox("Function to optimize", functions_to_optimize.keys())]

    start_points = {
        "(-1, -2)": np.matrix([[-1.], [-2.]]),
        "(-4, -5)": np.matrix([[-4.], [-5.]]),
        "(4, 5)": np.matrix([[4.], [5.]])
    }
    x = start_points[st.selectbox("Start point", start_points)]

    st.write(f"minimum:{method(f=function_to_optimize, x=x, config=config)}")


if __name__ == '__main__':
    two_argument_form(hydra.compose(config_name="config"))
