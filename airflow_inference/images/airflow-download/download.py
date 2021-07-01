import os
import typing

import click
from sklearn.datasets import load_diabetes


@click.command('download')
@click.option(
    '--output_dir',
    help = 'Output directory to save generated dataset',
    default = '/data/raw',
)
def download(
    output_dir: str,
) -> typing.NoReturn:

    X, y = load_diabetes(
        return_X_y = True,
        as_frame = True,
    )

    os.makedirs(
        name = output_dir,
        exist_ok = True,
    )

    save_path = os.path.join(output_dir, 'data.csv')
    X.to_csv(
        path_or_buf = save_path,
        index = False,
    )

    print(f'Write data.csv to {save_path}.')

    save_path = os.path.join(output_dir, 'target.csv')

    y.to_csv(
        path_or_buf = os.path.join(output_dir, 'target.csv'),
        index = False,
    )

    print(f'Write target.csv to {save_path}.')


if __name__ == '__main__':
    download()