from __future__ import annotations

import typing
import logging
import importlib

import numpy
import pandas
import joblib

from entities import (
    ModuleParams,
    ProcessParams,
    FeatureParams,
)

from modules.io import (
    load_module,
    save_module,
)


logger = logging.getLogger(__name__)


class Pipeline:

    def __init__(
        self,
        modules: typing.List[typing.Tuple[str, typing.ClassVar]],
        fitted: bool = False,
    ) -> Pipeline:

        if len(modules) == 0:
            logger.error('Pipeline initialisation is empty')

        self.fitted  = fitted
        self.modules = modules

    def fit(
        self,
        data: pandas.DataFrame,
    ) -> typing.NoReturn:

        for name, module in self.modules:
            module.fit(data)

        self.fitted  = True

    def transform(
        self,
        data: pandas.DataFrame,
    ) -> numpy.ndarray:

        if not self.fitted:
            logger.error('Pipeline was not fitted before using')

        transformed_data = data

        for name, module in self.modules:

            transformed_data = module.transform(transformed_data)

        return transformed_data

    def fit_transform(
        self,
        data: pandas.DataFrame,
    ) -> numpy.ndarray:

        self.fit(data)

        return self.transform(data)


class Transformer:

    def __init__(
        self,
        modules: typing.List[typing.Tuple[str, typing.ClassVar, typing.List[str]]],
        fitted: bool = False,
    ) -> Transformer:

        if len(modules) == 0:
            logger.error('Transformer initialisation is empty')

        self.fitted  = fitted
        self.modules = modules

    def fit(
        self,
        data: pandas.DataFrame,
    ) -> typing.NoReturn:

        for name, module, columns in self.modules:
            module.fit(data[columns])

        self.fitted  = True

    def transform(
        self,
        data: pandas.DataFrame,
    ) -> numpy.ndarray:

        if not self.fitted:
            logger.error('Transformer was not fitted before using')

        transformed_data = [
             module.transform(data[columns])
            for name, module, columns in self.modules
        ]

        return numpy.hstack(transformed_data)

    def fit_transform(
        self,
        data: pandas.DataFrame,
    ) -> numpy.ndarray:

        self.fit(data)

        return self.transform(data)
        

def build_pipeline(
    module_params: typing.List[ModuleParams],
    fitted:        bool = False,
) -> Pipeline:

    modules = []
    
    for module_param in module_params:

        module = load_module(module_param)

        modules.append(
            (module_param.name, module)
        )

    pipeline = Pipeline(
        modules = modules,
        fitted  = fitted,
    )

    logger.info(f'{pipeline.__class__.__name__} was build')

    return pipeline


def save_pipeline(
    pipeline:      Pipeline,
    module_params: typing.List[ModuleParams],
) -> typing.NoReturn:

    for i, (_, module) in enumerate(pipeline.modules):

        module_param = module_params[i]

        save_module(module, module_param)

    logger.info(f'{pipeline.__class__.__name__} was saved')


def build_transformer(
    process_params: ProcessParams,
    feature_params: FeatureParams,
    fitted:         bool = False,
) -> Transformer:

    transformer = Transformer(
        modules = [
            (
                feature_name,
                build_pipeline(
                    module_params = getattr(process_params, feature_name),
                    fitted        = fitted,
                ),
                [feature.name for feature in getattr(feature_params, feature_name)],

            )
        for feature_name in ('categorical', 'numerical')
        ],
        fitted = fitted
    )

    logger.info(f'{transformer.__class__.__name__} was build')

    return transformer


def save_transformer(
    transformer:    Transformer,
    process_params: ProcessParams,
) -> typing.NoReturn:

    for feature_name, modules, _ in transformer.modules:

        modules_params = getattr(process_params, feature_name)

        save_pipeline(
            pipeline      = modules,
            module_params = modules_params,
        )

    logger.info(f'{transformer.__class__.__name__} was saved')
