from __future__ import annotations

import numpy
import typing

from modules.models.base import BaseModel
from modules.io import (
    load_module,
    save_module,
)

class Model(BaseModel):

    def __init__(
        self,
        config_path: str,
    ) -> Model:

        super().__init__(config_path)

        self.module = load_module(self.params)


    def train(
        self,
        data: typing.Tuple[numpy.ndarray],
    ) -> typing.NoReturn:

        self.module.fit(*data)


    def eval(
        self,
        data: typing.Tuple[numpy.ndarray],
    ) -> typing.NoReturn:

        features, answers = data

        predictions = self.module.predict(features)


    def save(
        self,
    ) -> typing.NoReturn:

        save_module(
            module       = self.module,
            module_param = self.params,
        )