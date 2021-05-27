import typing
import logging

import click
import numpy
import pandas
import requests

from entities import (
    BaseLoader,
    FeaturesParams,
    MainParams,
)

from logs import setup_logging


logger = logging.getLogger(__name__)
OK = 200


def create_array_in_bounds(
    n_samples: int,
    min_value: typing.Union[int, float],
    max_value: typing.Union[int, float],
) -> numpy.ndarray:
    
    zero_one = numpy.random.random(n_samples)
    expanded = zero_one*(max_value - min_value) + min_value

    return expanded


def make_data(
    features: FeaturesParams,
    n_samples: int,
) -> typing.Tuple[pandas.DataFrame]:

    categorical_data = pandas.DataFrame({
        feature.name: create_array_in_bounds(
            n_samples,
            feature.min_value,
            feature.max_value,
        ).astype(numpy.int32)

        for feature in features.categorical
    })

    numerical_data = pandas.DataFrame({
        feature.name: create_array_in_bounds(
            n_samples,
            feature.min_value,
            feature.max_value,
        ).astype(numpy.float32)

        for feature in features.numerical
    })

    return categorical_data, numerical_data


@click.command(name = 'Make a request with fake data')
@click.option(
    '--n_samples',
    default = 1,
    type = click.IntRange(0, 10000),
    help = 'How many n_samples should I generate?',
)
@click.option(
    '--host',
    default = '0.0.0.0',
    help    = 'Host adress',
)
@click.option(
    '--port',
    default = 8000,
    help    = 'Port adress',
)
@click.option(
    '--log_config',
    default = 'configs/logs/request.yaml',
    help    = 'Path to log config',
)
def main(
    n_samples: int,
    host: str,
    port: int,
    log_config: str,
) -> typing.NoReturn:
    
    setup_logging(log_config)

    features = BaseLoader(FeaturesParams).read_params()

    cat, num = make_data(
        features,
        n_samples,
    )

    for i in range(n_samples):

        request = {

            'numerical_data': [num.iloc[i].tolist()],
            'numerical_names': list(num.columns),

            'categorical_data': [cat.iloc[i].tolist()],
            'categorical_names': list(cat.columns),

        }

        logger.info('Request has been sent, waiting for response')

        response = requests.get(
            url = f'http://{host}:{port}/predict',
            json = request,
        )

        logger.info('Response has been received, start checking')

        if response.status_code != OK:
            logger.error(f'Expected status_code: {OK}, received: {response.status_code}')

        logger.info('Response has been checked, all are ok')


if __name__ == '__main__':
    main()