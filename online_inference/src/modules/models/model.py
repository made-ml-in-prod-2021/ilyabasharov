from __future__ import annotations

import os
import numpy
import typing
import logging
import sklearn

from entities import (
    BaseLoader,
    ModuleParams,
    ProcessParams,
    FeatureParams,
)

from modules.process.preprocess import Preprocess
from modules.models.base import BaseModel
from modules.io import load_module

logger = logging.getLogger(__name__)


class Model(BaseModel):

    def __init__(
        self,
    ) -> Model:

        super().__init__()

        self.model = None
        self.process = None


    def load(
        self,
        model_config: str,
        process_config: str,
        feature_params: FeatureParams,
        fitted:         bool = False,
    ) -> typing.NoReturn:

        self.model_params = BaseLoader(ModuleParams).read_params(model_config)
        self.model = load_module(self.model_params)

        self.process = Preprocess(
            process_config,
            feature_params,
            fitted
        )
       
    def test(
        self,
        features: pandas.DataFrame,
    ) -> numpy.ndarray:

        features = self.process.to_eval(features)

        return self.model.predict(features)
