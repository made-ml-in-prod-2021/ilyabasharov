import dataclasses


@dataclasses.dataclass()
class ModuleParams:
    name:        str
    import_from: str
    path:        str
    kwargs:      dict