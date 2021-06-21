from __future__ import annotations

import os
import typing
import logging

import yaml
import marshmallow_dataclass


DEFAULT_PATH = 'configs/entities'
logger = logging.getLogger(__name__)

class BaseLoader:

    def __init__(
        self,
        entity: typing.ClassVar,
    ) -> BaseLoader:

        self.shema = marshmallow_dataclass.class_schema(entity)
        self.path = os.path.join(DEFAULT_PATH, f'{entity.__name__}.yaml')

    def read_params(
        self,
        path: str = None,
    ) -> typing.ClassVar:

        if path is None:
            path = self.path

        if not os.path.exists(path):
            logger.error(f'Load config failed: {path} does not exit')

        with open(path, 'r') as file:

            container = self.shema()
            self.params = container.load(yaml.safe_load(file))

        logger.info(f'Config file {path} was loaded')

        return self.params