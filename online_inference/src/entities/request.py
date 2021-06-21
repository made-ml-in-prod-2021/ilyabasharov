import typing
import logging

import pydantic

from .loader import BaseLoader
from .features import FeaturesParams


logger = logging.getLogger(__name__)

features = BaseLoader(FeaturesParams).read_params()

class Request(pydantic.BaseModel):

    numerical_data: pydantic.conlist(
        pydantic.conlist(
            typing.Union[float],
            min_items = len(features.numerical),
            max_items = len(features.numerical),
        ),
        min_items = 1,
    )

    numerical_names: pydantic.conlist(
        str,
        min_items = len(features.numerical),
        max_items = len(features.numerical),
     )

    categorical_data: pydantic.conlist(
        pydantic.conlist(
            typing.Union[int],
            min_items = len(features.categorical),
            max_items = len(features.categorical),
        ),
        min_items = 1,
    )

    categorical_names: pydantic.conlist(
        str,
        min_items = len(features.categorical),
        max_items = len(features.categorical),
     )

    @pydantic.root_validator()
    def check_n_samples(
        cls,
        data: typing.Dict[str, typing.Any],
    ) -> typing.Dict[str, typing.Any]:

        numerical = data.get('numerical_data')
        categorical = data.get('numerical_data')

        if numerical is None or categorical is None:
            logger.error('Request data is empty')

        if len(numerical) != len(categorical):
            logger.error('Number of samples are not equal')

        return data

    @pydantic.validator('categorical_names')
    def check_categorical_feature_names(
        cls,
        data: typing.List[str],
    ) -> typing.List[str]:

        for got, feature_info in zip(data, features.categorical):
            expected = feature_info.name
            if got != expected:
                logger.error(
                    f'Сategorical feature names are not equal: expected - {expected}, got - {got}'
                )

        return data

    @pydantic.validator('numerical_names')
    def check_numerical_feature_names(
        cls,
        data: typing.List[str],
    ) -> typing.List[str]:

        for got, feature_info in zip(data, features.numerical):
            expected = feature_info.name
            if got != expected:
                logger.error(
                    f'Numerical names are not equal: expected - {expected}, got - {got}'
                )

        return data


    @pydantic.validator('numerical_data')
    def check_numerical_in_bounds(
        cls, 
        data: typing.List[typing.List[float]],
    ) -> typing.List[typing.List[float]]:

        for sample in data:
            for value, bounds in zip(sample, features.numerical):

                if not (bounds.min_value <= value <= bounds.max_value):
                    logger.error(
                        f'Numerical value {value} not in the bounds [{bounds.min_value}, {bounds.max_value}]'
                    )



        return data

    @pydantic.validator('categorical_data')
    def check_categorical_in_bounds(
        cls,
        data: typing.List[typing.List[int]],
    ) -> typing.List[typing.List[int]]:

        for sample in data:
            for value, bounds in zip(sample, features.categorical):

                if not (bounds.min_value <= value <= bounds.max_value):
                    logger.error(
                        f'Categorical value {value} not in the bounds [{bounds.min_value}, {bounds.max_value}]'
                    )

        return data
