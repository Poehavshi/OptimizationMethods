import logging

import hydra
import streamlit as st
from omegaconf import DictConfig

from ..controllers.basic_methods import find_min_by_gold
from ..models.functions_of_one_argument import *

log = logging.getLogger(__name__)


def main(config: DictConfig):
    log.info("START APP")
    st.title("Functions of one argument")
    st.text(f"{find_min_by_gold(-10, 10, f1, epsilon=config.epsilon, precision=config.precision, n=config.N)}")


if __name__ == '__main__':
    main(hydra.compose(config_name="config"))
