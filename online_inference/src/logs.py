import typing
import logging.config

import yaml


def setup_logging(
    config_path: str,
) -> typing.NoReturn:

    '''Logger from yaml config.'''

    with open(config_path, 'r') as file:
        logging.config.dictConfig(yaml.safe_load(file))