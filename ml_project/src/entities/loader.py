from __future__ import annotations

import yaml
import typing
import marshmallow_dataclass


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

        with open(path, 'r') as file:

            container = self.shema()
            self.params = container.load(yaml.safe_load(file))

        return self.params