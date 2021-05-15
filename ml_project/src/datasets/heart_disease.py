from __future__ import annotations

import typing
import pandas

from sklearn.model_selection import train_test_split

from entities import FeatureParams
from modules import Preprocess

from datasets.base import BaseDataset


class HeartDeseaseDataset(BaseDataset):

    def __init__(
        self,
        config_path_dataset: str,
        config_path_process: str,
    ) -> HeartDeseaseDataset:

        super().__init__(config_path_dataset)

        self.data = get_data(
            data_path   = self.params.path,
            split_param = self.params.split,
        )

        self.preprocess = Preprocess(
            config_path    = config_path_process,
            feature_params = self.params.features,
        )

    def to_train(
        self,
    ) -> typing.Tuple[numpy.ndarray]:

        features = self.preprocess.to_train(self.data['train'])
        answers  = self.data['train'][self.params.features.target].to_numpy().ravel()

        return features, answers

    def to_eval(
        self,
    ) -> typing.Tuple[numpy.ndarray]:

        features = self.preprocess.to_eval(self.data['val'])
        answers  = self.data['val'][self.params.features.target].to_numpy().ravel()

        return features, answers


def get_data(
    data_path:   str,
    split_param: SplitParams,
) -> typing.Dict[str, pandas.DataFrame]:

    raw = pandas.read_csv(data_path)

    data = dict()

    data['train'], data['val'] = train_test_split(
        raw,
        train_size   = split_param.train_size,
        test_size    = split_param.val_size,
        random_state = split_param.random_state,
        shuffle      = split_param.shuffle,
    )

    return data
