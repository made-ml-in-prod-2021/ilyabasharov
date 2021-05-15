from __future__ import annotations

import numpy
import typing
import pandas

from entities import (
    BaseLoader,
    ProcessParams,
    FeatureParams,
)


class BaseProcess:

    def __init__(
        self,
        config_path: str,
    ) -> BaseProcess:

        self.params = BaseLoader(ProcessParams).read_params(config_path)

        pass


    def to_train(
        self,
        data: pandas.DataFrame,
    ) -> numpy.ndarray:

        pass
        

    def to_eval(
        self,
        data: pandas.DataFrame,
    ) -> numpy.ndarray:

        pass


    def save(
        self,
    ) -> typing.NoReturn:

        pass