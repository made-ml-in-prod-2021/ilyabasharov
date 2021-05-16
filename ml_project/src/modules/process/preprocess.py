from __future__ import annotations

import typing
import pandas
import sklearn

from entities import FeatureParams

from .base import BaseProcess
from .build_features import (
    build_transformer,
    save_transformer,
)


class Preprocess(BaseProcess):

    def __init__(
        self,
        config_path:    str,
        feature_params: FeatureParams,
        fitted:         bool = False,
    ) -> Preprocess:

        super().__init__(config_path)

        self.process = build_transformer(
            process_params = self.params,
            feature_params = feature_params,
            fitted         = fitted,
        )

    def to_train(
        self,
        data: pandas.DataFrame,
    ) -> np.ndarray:

        return self.process.fit_transform(data)


    def to_eval(
        self,
        data: pandas.DataFrame,
        ) -> np.ndarray:

        return self.process.transform(data)


    def save(
        self,
    ) -> typing.NoReturn:

        save_transformer(
            transformer    = self.process,
            process_params = self.params,
        )
