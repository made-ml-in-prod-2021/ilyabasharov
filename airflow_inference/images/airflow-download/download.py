import os
import typing

import click
from sklearn.datasets import load_diabetes


@click.command('download')
@click.option(
    '--output_dir',
    help = 'Output directory to save generated dataset',
    default = 'data/raw',
)
def download(
    output_dir: str,
) -> typing.NoReturn:

    X, y = load_diabetes(
        return_X_y=True,
        as_frame=True,
    )

    os.makedirs(
        name = output_dir,
        exist_ok = True,
    )

    X.to_csv(
        path_or_buf = os.path.join(output_dir, 'data.csv'),
        index = False,
    )

    y.to_csv(
        path_or_buf = os.path.join(output_dir, 'target.csv'),
        index = False,
    )


if __name__ == '__main__':
    download()