from __future__ import annotations

import numpy
import typing

from entities import (
    BaseLoader,
    ModuleParams,
)


class BaseModel:

    def __init__(
        self,
    ) -> BaseModel:

        pass

    def load(
        self,
        model_config: str,
        process_config: str,
    ) -> typing.NoReturn:

        pass


    def train(
        self,
        data: typing.Tuple[numpy.ndarray],
    ) -> typing.NoReturn:

        pass

    
    def eval(
        self,
        data: typing.Tuple[numpy.ndarray],
    ) -> typing.NoReturn:

        pass


    def test(
        self,
        features: numpy.ndarray,
    ) -> typing.NoReturn:

        pass


    def save(
        self,
    ) -> typing.NoReturn:

        pass