import dataclasses


@dataclasses.dataclass()
class MainParams:
    model:      str
    dataset:    str
    preprocess: str
    logs:       str