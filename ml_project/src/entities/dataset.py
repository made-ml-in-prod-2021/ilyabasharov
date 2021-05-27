import dataclasses

from entities.split import SplitParams
from entities.features import FeatureParams


@dataclasses.dataclass()
class DatasetParams:
    path:     str
    split:    SplitParams
    features: FeatureParams
