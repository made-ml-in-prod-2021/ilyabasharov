import click
import numpy
import typing
import pandas


def generate_as(
    data:         pandas.DataFrame,
    n_samples:    int,
) -> pandas.DataFrame:
    
    fake_data = dict()

    for feature_name in data.columns:

        zero_one  = numpy.random.random(n_samples)
        max_value = data[feature_name].max()
        min_value = data[feature_name].min()

        fake = zero_one*(max_value - min_value) + min_value

        fake_data[feature_name] = fake.astype(data[feature_name].dtype)

    return pandas.DataFrame(fake_data)


@click.command()
@click.option(
    '--n_samples',
    default = 1000,
    help    = 'How many n_samples should I generate?',
)
@click.option(
    '--original_data_path',
    default = 'datasets/raw/heart_disease.csv',
    help    = 'Where I should get an original_data?',
)
@click.option(
    '--save_path',
    default = 'datasets/fake/fake.csv',
    help    = 'Where I should save fake dataset?',
)
def generate(
    n_samples:          int,
    save_path:          str,
    original_data_path: str,
) -> typing.NoReturn:
    
    '''Dataset generator based on original dataset via NumPy library'''

    original_data = pandas.read_csv(original_data_path)

    fake_data = generate_as(original_data, n_samples)

    fake_data.to_csv(save_path)


if __name__ == '__main__':
    generate()