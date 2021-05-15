import typing
import dataclasses

from entities.module import ModuleParams


@dataclasses.dataclass()
class ProcessParams:
    categorical: typing.List[ModuleParams]
    numerical:   typing.List[ModuleParams]