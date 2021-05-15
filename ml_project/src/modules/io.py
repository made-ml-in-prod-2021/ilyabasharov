import os
import joblib
import typing
import importlib

from entities import ModuleParams

def load_module(
    module_param: ModuleParams,
) -> typing.ClassVar:

    if os.path.exists(module_param.path):
        module = joblib.load(module_param.path)
    else:
        import_from = importlib.import_module(module_param.import_from)
        module = getattr(import_from, module_param.name)(**module_param.kwargs)

    return module

def save_module(
    module: typing.ClassVar,
    module_param: ModuleParams,
) -> typing.NoReturn:

    joblib.dump(
        value    = module,
        filename = module_param.path,
    )
