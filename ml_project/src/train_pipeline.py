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
    default = 'configs/main.yaml',
    help    = 'path to config file with model, dataset, preprocess',)
def train_pipeline(
    config: str
) -> typing.NoReturn:

    ''' It starts the main train pipeline '''

    args = BaseLoader(MainParams).read_params(config)

    dataset = HeartDeseaseDataset(
        config_path_dataset = args.dataset,
        config_path_process = args.preprocess,
    )

    model = Model(args.model)

    # train stage

    data = dataset.to_train()
    model.train(data)

    # val stage

    data = dataset.to_eval()
    model.eval(data)

    # save stage

    model.save()
    dataset.preprocess.save()


if __name__ == '__main__':
    train_pipeline()