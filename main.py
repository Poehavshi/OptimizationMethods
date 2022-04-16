import runpy
import os

import logging

import hydra
from hydra.core.global_hydra import GlobalHydra
from hydra.utils import get_original_cwd
from omegaconf import DictConfig

log = logging.getLogger(__name__)


@hydra.main(config_path="./conf", config_name="config")
def main(config: DictConfig):
    os.chdir(get_original_cwd())
    runpy.run_module("app.views.one_argument_examples", run_name="__main__", alter_sys=True)


if __name__ == '__main__':
    main()
