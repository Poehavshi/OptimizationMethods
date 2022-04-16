import logging

import hydra
import streamlit as st
from omegaconf import DictConfig


log = logging.getLogger(__name__)


def two_argument_form(config: DictConfig):
    st.title("Functions of two and more arguments")


if __name__ == '__main__':
    two_argument_form(hydra.compose(config_name="config"))
