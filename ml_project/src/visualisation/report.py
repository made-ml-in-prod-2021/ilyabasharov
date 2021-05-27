import yaml
import click
import pandas
import typing
import logging
import pandas_profiling

from src.logs import setup_logging

logger = logging.getLogger(__name__)


@click.command()
@click.option(
    '--dataset_path',
    default = 'datasets/raw/heart_disease.csv',
    help    = 'path to a dataset',
)
@click.option(
    '--save_path',
    default = 'logs/report.html',
    help    = 'path to config file with model, dataset, preprocess',
)
@click.option(
    '--log_config',
    default = 'configs/logs/report.yaml',
    help    = 'path to logging config',
)
def report(
    dataset_path: str,
    save_path:    str,
    log_config:   str,
) -> typing.NoReturn:

    '''It starts a report creation based on '''

    setup_logging(log_config)

    logger.info(f'Start reading the dataset {dataset_path}')
    data = pandas.read_csv(dataset_path)
    logger.info(f'Done reading the dataset {dataset_path}')

    logger.info(f'The report begins to be written based on {dataset_path}')
    profile = pandas_profiling.ProfileReport(data)
    profile.to_file(output_file=save_path)
    logger.info(f'The report was written to {save_path}')


if __name__ == '__main__':
    report()