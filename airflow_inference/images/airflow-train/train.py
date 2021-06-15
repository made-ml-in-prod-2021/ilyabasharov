import os
import typing

import click
import joblib

import pandas as pd
from sklearn.ensemble import RandomForestRegressor


def prepare_data(
    df: pd.DataFrame,
    target: str,
) -> typing.Tuple[pd.DataFrame]:

    target = df[target]
    df.drop(
        labels = [target],
        axis = 1,
        inplace = True,
    )

    return df, target


def train_model(
    x: pd.DataFrame,
    y: pd.DataFrame,
) -> typing.ClassVar:

    clf = RandomForestRegressor(
        n_estimators = 100,
    )

    clf.fit(x, y)

    return clf


@click.command('train')
@click.option(
    '--data_dir',
    help = 'Data path of preprocessed data',
    default = 'data/pure/',
)
@click.option(
    '--model_dir',
    help = 'Where should save the model',
    default = 'data/model/',
)
def train(
    data_dir: str,
    model_dir: str
):
    data_path = os.path.join(data_dir, 'train_data.csv')
    data = pd.read_csv(data_path)

    x, y = prepare_data(data)
    model = train_model(x, y)

    os.makedirs(
        name = model_dir,
        exist_ok = True,
    )

    model_save_path = os.path.join(model_dir, 'model.pkl')

    joblib.dump(
        value = model,
        filename = model_save_path,
    )


if __name__ == '__main__':
    train()