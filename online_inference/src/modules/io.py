import os
import typing
import logging
import importlib

import joblib

from entities import ModuleParams


logger = logging.getLogger(__name__)


def load_module(
    module_param: ModuleParams,
) -> typing.ClassVar:

    if os.path.exists(module_param.path):
        module = joblib.load(module_param.path)

        logger.info(
            f'{module.__class__.__name__} was loaded from {module_param.path}'
        )

    else:
        import_from = importlib.import_module(module_param.import_from)
        module = getattr(import_from, module_param.name)(**module_param.kwargs)

        logger.info(
            f'{module.__class__.__name__} was created from {module_param.import_from}'
        )

    return module

def save_module(
    module: typing.ClassVar,
    module_param: ModuleParams,
) -> typing.NoReturn:

    dirname, filename = os.path.split(module_param.path)

    if os.path.exists(dirname):
        joblib.dump(
            value    = module,
            filename = module_param.path,
        )
        logger.info(
            f'{module.__class__.__name__} was dumped into {module_param.path}'
        )

    else:
        logger.error(
            f'{module.__class__.__name__} dump failed: directory {dirname} for {filename} does not exist'
        )