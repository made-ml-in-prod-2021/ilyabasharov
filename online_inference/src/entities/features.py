import math
import typing
import dataclasses


@dataclasses.dataclass()
class FeatureParams:
	name: str
	min_value: typing.Union[int, float]
	max_value: typing.Union[int, float]

	
@dataclasses.dataclass()
class FeaturesParams:
	categorical: typing.List[FeatureParams]
	numerical: typing.List[FeatureParams]
	target: typing.List[FeatureParams]



