import typing
import logging

import pydantic

from .loader import BaseLoader
from .features import FeaturesParams


logger = logging.getLogger(__name__)
features = BaseLoader(FeaturesParams).read_params()


class Response(pydantic.BaseModel):

    ids: typing.List[int]
    targets: typing.List[int]


    @pydantic.validator('ids')
    def check_ids(
        cls,
        data: typing.List[int],
    ) -> typing.List[int]:

        return data


    @pydantic.validator('targets')
    def check_targets(
        cls,
        data: typing.List[int],
    ) -> typing.List[int]:

        bounds = features.target[0]

        for value in data:
            if not (bounds.min_value <= value <= bounds.max_value):
                logger.error(f'Target value {value} not in the bounds [{bounds.min_value}, {bounds.max_value}]')

        return data