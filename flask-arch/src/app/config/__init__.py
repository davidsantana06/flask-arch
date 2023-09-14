from flask import Flask
from importlib import import_module
from inspect import isfunction
from os import (
    path,
    listdir
)
from types import FunctionType, ModuleType
from typing import List
from app.constants import APP_FOLDER_PATH


__CONFIG_DIRECTORY: str = path.join(APP_FOLDER_PATH, 'config')
__CONFIG_MODULE_PATH: str = 'app.config.{module_name}'


def configure_all(app: Flask) -> None:
    configure_functions: List[FunctionType] = []

    modules: List[str] = [
        file_name[:-3] for file_name in listdir(__CONFIG_DIRECTORY)
        if (file_name.endswith('.py')) and (not file_name.startswith('__'))
    ]

    for module_name in modules:
        module: ModuleType = import_module(
            __CONFIG_MODULE_PATH.format(module_name=module_name)
        )

        for name, item in module.__dict__.items():
            if (name.startswith('configure')) and (isfunction(item)):
                configure_functions.append(item)

    for configure_function in configure_functions:
        configure_function(app)
