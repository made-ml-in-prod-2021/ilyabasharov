import typing
import dataclasses

from .module import ModuleParams


@dataclasses.dataclass()
class ProcessParams:
    categorical: typing.List[ModuleParams]
    numerical:   typing.List[ModuleParams]