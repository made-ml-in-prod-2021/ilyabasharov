import dataclasses


@dataclasses.dataclass()
class MainParams:
    model: str
    preprocess: str
    logs: str