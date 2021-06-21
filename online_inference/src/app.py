import typing
import logging
import datetime

import click
import pandas
import fastapi
import uvicorn

from logs import setup_logging

from entities import (
    BaseLoader,
    MainParams,
    FeaturesParams,
    Response,
    Request,
)

from modules import Model

start_time = None
max_time = 30
logger = logging.getLogger(__name__)
args = BaseLoader(MainParams).read_params()
features = BaseLoader(FeaturesParams).read_params()
app = fastapi.FastAPI()
model = Model()
model.load(
    model_config = args.model,
    process_config = args.preprocess,
    feature_params = features,
    fitted = True,
)


def make_predict(
    categorical_data: typing.List[typing.List[int]],
    categorical_names: typing.List[str],
    numerical_data: typing.List[typing.List[float]],
    numerical_names: typing.List[str],
    model,
) -> Response:

    logger.debug('Start making a predict')

    categorical = pandas.DataFrame(categorical_data, columns=categorical_names)
    numerical = pandas.DataFrame(numerical_data, columns=numerical_names)

    full = pandas.concat([categorical, numerical], axis=1)

    predicts = model.test(full)

    ret = Response(
        ids = list(range(len(predicts))),
        targets = predicts.tolist(),
    )

    logger.debug('Make a predict: done')

    return ret


@app.get('/')
def main(
) -> str:

    global start_time, max_time

    logger.debug('start main')
    logger.info('request on /')
    

    if start_time is None:
        start_time = datetime.datetime.now()

    delta = (datetime.datetime.now() - start_time).seconds

    if delta > max_time:
        raise Exception('App was killed by timeout')

    string = f'It is entry  point of my predictor. Will be killed after {max_time - delta} sec.'
    logger.debug('stop main')

    return string


@app.get('/predict', response_model = Response)
def predict(
    request: Request,
) -> Response:

    logger.debug('start predict')
    logger.info('request on /predict')

    predicted = make_predict(
        request.categorical_data,
        request.categorical_names,
        request.numerical_data,
        request.numerical_names,
        model,
    )

    logger.debug('stop predict')

    return predicted


@app.exception_handler(fastapi.exceptions.RequestValidationError)
async def validation_exception_handler(
    request,
    exception,
) -> fastapi.responses.JSONResponse:

    responce =  fastapi.responses.JSONResponse(
        status_code = 400,
        content = fastapi.encoders.jsonable_encoder(
            {
                'trace': exception.errors(),
                'body': exception.body,
            }
        ),
    )

    return responce

@app.on_event('startup')
async def load_model(
) -> typing.NoReturn:

    logger.debug('Start loading the model')

    features = BaseLoader(FeaturesParams).read_params()

    global model
    model.load(
        model_config = args.model,
        process_config = args.preprocess,
        feature_params = features,
        fitted = True,
    )

    logger.debug('Loading the model: done')


@click.command(name = 'Connection setup')
@click.option(
    '--host',
    default = '0.0.0.0',
    help    = 'host adress',
)
@click.option(
    '--port',
    default = 8000,
    help    = 'port adress',
)
def main(
    host: str,
    port: int,
) -> typing.NoReturn:

    ''' Main script for running the online inference '''

    setup_logging(args.logs)

    uvicorn.run(
        'app:app',
        host = host,
        port = port,
        debug = True,
    )


if __name__ == '__main__':
    main()