import click
import typing
import logging

from entities import (
    BaseLoader,
    MainParams,
)

from datasets import HeartDeseaseDataset
from modules import Model
from logs import setup_logging

logger = logging.getLogger(__name__)


@click.command()
@click.option(
    '--config',
    default = 'configs/train.yaml',
    help    = 'path to config file with model, dataset, preprocess',
)
@click.option(
    '--save',
    default = True,
    is_flag = True,
    help    = 'save all used pipeline',
)
def train(
    config: str,
    save:   bool,
) -> typing.NoReturn:

    ''' It starts the main train/val pipeline '''

    args = BaseLoader(MainParams).read_params(config)

    setup_logging(args.logs)

    dataset = HeartDeseaseDataset(
        config_path_dataset = args.dataset,
        config_path_process = args.preprocess,
    )

    model = Model(args.model)

    # train stage

    data = dataset.to_train()
    model.train(data)

    # val stage

    data = dataset.to_val()
    model.eval(data)

    # save stage

    if save:
        model.save()
        dataset.preprocess.save()


if __name__ == '__main__':
    train()