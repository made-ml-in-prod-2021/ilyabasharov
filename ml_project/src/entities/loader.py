from __future__ import annotations

import os
import yaml
import typing
import logging
import marshmallow_dataclass

logger = logging.getLogger(__name__)

class BaseLoader:

    def __init__(
        self,
        entity: typing.ClassVar,
    ) -> BaseLoader:

        self.shema  = marshmallow_dataclass.class_schema(entity)

    def read_params(
        self,
        path: str,
    ) -> typing.ClassVar:

        if not os.path.exists(path):
            logger.error(f'Load config failed: {path} does not exit')

        with open(path, 'r') as file:

            container = self.shema()
            self.params = container.load(yaml.safe_load(file))

        logger.info(f'Config file {path} was loaded')

        return self.params