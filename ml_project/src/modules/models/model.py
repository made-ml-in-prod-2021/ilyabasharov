from __future__ import annotations

import os
import numpy
import typing
import logging
import sklearn

from sklearn.metrics import accuracy_score

from modules.models.base import BaseModel
from modules.io import (
    load_module,
    save_module,
)

logger = logging.getLogger(__name__)


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

        logger.info(f'{self.module.__class__.__name__} was fitted')


    def eval(
        self,
        data: typing.Tuple[numpy.ndarray],
    ) -> typing.NoReturn:

        features, answers = data

        try:
            predictions = self.module.predict(features)
            score = accuracy_score(answers, predictions)

            logger.info(f'{self.module.__class__.__name__} predicted with {score:.4f} score')

        except sklearn.exceptions.NotFittedError:

            logger.error(f'Fit the {self.module.__class__.__name__} before using')

    def test(
        self,
        features: numpy.ndarray,
    ) -> typing.NoReturn:


        try:
            predictions = self.module.predict(features)
            save_predictions(self.params.save_preds, predictions)

        except sklearn.exceptions.NotFittedError:

            logger.error(f'Fit the {self.module.__class__.__name__} before using')


    def save(
        self,
    ) -> typing.NoReturn:

        save_module(
            module       = self.module,
            module_param = self.params,
        )

def save_predictions(
    save_path:        str,
    predictions: numpy.ndarray,
) -> typing.NoReturn:

    dirname, filename = os.path.split(save_path)

    if os.path.exists(dirname):
        numpy.savetxt(save_path, predictions, fmt='%i')

        logger.info(f'Predictions was saved to {save_path}')

    else:
        logger.error(f'Predictions save failed: path {save_path} does not exist')