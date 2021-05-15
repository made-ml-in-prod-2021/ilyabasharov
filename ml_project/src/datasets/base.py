from __future__ import annotations

import numpy
import typing

from entities import (
    BaseLoader,
    DatasetParams,
)


class BaseDataset:

    def __init__(
        self,
        config_path: str,
    ) -> BaseDataset:

        self.params = BaseLoader(DatasetParams).read_params(config_path)

        pass


    def to_train(
        self,
    ) -> typing.Tuple[numpy.ndarray]:

        pass


    def to_eval(
        self,
    ) -> typing.Tuple[numpy.ndarray]:

        pass