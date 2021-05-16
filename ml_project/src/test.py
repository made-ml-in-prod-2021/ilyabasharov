import click
import typing

from entities import (
    BaseLoader,
    MainParams,
)

from datasets import HeartDeseaseDataset
from modules import Model


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