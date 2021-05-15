import dataclasses


@dataclasses.dataclass()
class SplitParams:
    train_size:   float
    val_size:     float
    random_state: int
    shuffle:      bool