import logging
import hydra
from omegaconf import DictConfig

from app.views.one_argument_examples import one_argument_form
from app.views.two_argument_examples import two_argument_form

log = logging.getLogger(__name__)


@hydra.main(config_path="./conf", config_name="config")
def main(config: DictConfig):
    one_argument_form(config)
    two_argument_form(config)


if __name__ == '__main__':
    main()
