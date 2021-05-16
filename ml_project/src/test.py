import click
import typing
import logging

from entities import (
    BaseLoader,
    MainParams,
)

from datasets import HeartDeseaseDataset
from modules import Model
from src.logs import setup_logging

logger = logging.getLogger(__name__)


@click.command()
@click.option(
    '--config',
    default = 'configs/test.yaml',
    help    = 'path to config file with model, dataset, preprocess',
)
def test(
    config: str
) -> typing.NoReturn:

    ''' It starts the main test pipeline '''

    args = BaseLoader(MainParams).read_params(config)

    setup_logging(args.logs)

    dataset = HeartDeseaseDataset(
        config_path_dataset = args.dataset,
        config_path_process = args.preprocess,
        fitted              = True,
    )

    model = Model(args.model)

    # test stage

    data = dataset.to_test()

    model.test(data)


if __name__ == '__main__':
    test()