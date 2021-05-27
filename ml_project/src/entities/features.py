import typing
import dataclasses


@dataclasses.dataclass()
class FeatureParams:
    categorical: typing.List[str]
    numerical:  typing.List[str]
    target:     typing.List[str]