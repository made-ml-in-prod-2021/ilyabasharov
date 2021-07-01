import os
import typing

import click
import pandas as pd


@click.command('predict')
@click.option(
    '--data_dir',
    help = 'Path to read the data',
    default = '/data/raw/',
)
@click.option(
    '--output_dir',
    help = 'Path to save preprocessed data',
    default = '/data/pure/',
)
def preprocess(
    data_dir: str,
    output_dir: str,
) -> typing.NoReturn:

    data = pd.read_csv(os.path.join(data_dir, 'data.csv'))
    target = pd.read_csv(os.path.join(data_dir, 'target.csv'))

    os.makedirs(
        name = output_dir,
        exist_ok = True,
    )

    train_data = pd.concat(
        objs = [data, target],
        axis = 1,
    )

    train_data.to_csv(
        path_or_buf = os.path.join(output_dir, 'data.csv'),
        index = False,
    )


if __name__ == '__main__':
    preprocess()