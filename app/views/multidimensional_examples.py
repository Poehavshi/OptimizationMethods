import logging

import hydra
import streamlit as st
from omegaconf import DictConfig

from app.models.multi_dimensional_functions import QuadraticFunction, HyperbolicCosineFunction, AbstractFunction
from app.controllers.multi_dimensional_methods import coordinate_descent, gradient_descent, newton_descent

import numpy as np
import matplotlib.pyplot as plt

log = logging.getLogger(__name__)


def two_argument_form(config: DictConfig):
    st.title("Functions of two and more arguments")
    methods = [coordinate_descent, gradient_descent, newton_descent]
    method = st.selectbox("Optimization method", methods, format_func=lambda x: x.__name__)

    functions_to_optimize = {"quadratic": QuadraticFunction(), "hyperbolic": HyperbolicCosineFunction()}
    function_to_optimize = st.selectbox("Function to optimize", functions_to_optimize.keys())
    # st.write(f"minimum:{method((0.,0.), f, config)}")
    st.pyplot(create_plot(functions_to_optimize[function_to_optimize]))


def create_plot(function: AbstractFunction):
    x1 = np.linspace(-12, 12, 30)
    x2 = np.linspace(-12, 12, 30)
    x1, x2 = np.meshgrid(x1, x2)
    function_values = function(x1, x2)

    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ax.plot_surface(x1, x2, function_values, rstride=1, cstride=1,
                    cmap='viridis', edgecolor='none')
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('f')

    return fig


if __name__ == '__main__':
    two_argument_form(hydra.compose(config_name="config"))
