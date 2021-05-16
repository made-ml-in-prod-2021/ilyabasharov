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
        fitted:              bool = False
    ) -> HeartDeseaseDataset:

        super().__init__(config_path_dataset)

        self.data = get_data(
            data_path   = self.params.path,
            split_param = self.params.split,
        )

        self.preprocess = Preprocess(
            config_path    = config_path_process,
            feature_params = self.params.features,
            fitted         = fitted,
        )

    def to_train(
        self,
    ) -> typing.Tuple[numpy.ndarray]:

        features = self.preprocess.to_train(self.data['train'])
        answers  = self.data['train'][self.params.features.target].to_numpy().ravel()

        return features, answers

    def to_val(
        self,
    ) -> typing.Tuple[numpy.ndarray]:

        features = self.preprocess.to_eval(self.data['val'])
        answers  = self.data['val'][self.params.features.target].to_numpy().ravel()

        return features, answers

    def to_test(
        self,
    ) -> numpy.ndarray:

        return self.preprocess.to_eval(self.data['all'])


def get_data(
    data_path:   str,
    split_param: SplitParams,
) -> typing.Dict[str, pandas.DataFrame]:

    data = dict()

    data['all'] = pandas.read_csv(data_path)

    data['train'], data['val'] = train_test_split(
        data['all'],
        train_size   = split_param.train_size,
        test_size    = split_param.val_size,
        random_state = split_param.random_state,
        shuffle      = split_param.shuffle,
    )

    return data
