import typing
import joblib
import importlib

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from entities import (
    ModuleParams,
    ProcessParams,
    FeatureParams,
)

from modules.io import (
    load_module,
    save_module,
)


def build_pipeline(
    module_params: typing.List[ModuleParams],
) -> Pipeline:

    modules = []
    
    for module_param in module_params:

        module = load_module(module_param)

        modules.append(
            (module_param.name, module)
        )

    pipeline = Pipeline(modules)

    return pipeline


def save_pipeline(
    pipeline:      Pipeline,
    module_params: typing.List[ModuleParams],
) -> typing.NoReturn:

    for i in range(len(module_params)):

        _, module    = pipeline.steps[i]
        module_param = module_params[i]

        save_module(module, module_param)


def build_transformer(
    process_params: ProcessParams,
    feature_params: FeatureParams,
) -> ColumnTransformer:

    transformer = ColumnTransformer(
        [
            (
                feature_name,
                build_pipeline(getattr(process_params, feature_name)),
                getattr(feature_params, feature_name),

            )
        for feature_name in ('categorical', 'numerical')
        ]
    )

    return transformer


def save_transformer(
    transformer:    ColumnTransformer,
    process_params: ProcessParams,
) -> typing.NoReturn:

    for feature_name in ('categorical', 'numerical'):

        modules_params = getattr(process_params, feature_name)
        modules        = transformer.named_transformers_[feature_name]

        save_pipeline(
            pipeline     = modules,
            module_params = modules_params,
        )
