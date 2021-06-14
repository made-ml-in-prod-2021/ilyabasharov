import os
import typing

import click
import joblib
import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestRegressor


def load_model(
    model_path: str,
) -> typing.ClassVar:

    model = joblib.load(model_path)

    return model


def save_predictions(
    preds: np.ndarray,
    output_path: str,
) -> typing.NoReturn:

    y = pd.DataFrame({'target': preds})

    y.to_csv(
        path_or_buf = output_path,
        index = False,
        header = None,
    )


@click.command('predict')
@click.option(
    '--data_dir',
    help = 'path to raw data',
    default = 'data/raw/',
)
@click.option(
    '--model_dir',
    help = 'path to saved model',
    default = 'data/model/',
)
@click.option(
    '--prediction_dir',
    help = 'path to saved model',
    default = 'data/model/',
)
def predict(
    data_dir: str,
    model_dir: str,
    prediction_dir: str
) -> typing.NoReturn:

    data_path = os.path.join(data_dir, 'data.csv')
    data = pd.read_csv(data_path)

    model_path = os.path.join(model_dir, 'model.pkl')
    model = load_model(model_path)

    preds = model.predict(data)
    os.makedirs(
        name = prediction_dir,
        exist_ok = True,
    )

    preds_path = os.path.join(prediction_dir, 'predictions.csv')
    
    save_predictions(
        preds = preds,
        output_path = preds_path,
    )


if __name__ == '__main__':
    predict()