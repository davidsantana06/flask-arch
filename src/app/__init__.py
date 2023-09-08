from app.core.constants import APP_FOLDER_PATH

from flask import Blueprint, Flask
from importlib import import_module
from os import (
    listdir, 
    path
)


def configure_app(app: Flask) -> None:
    pass


def configure_context_processors(app: Flask) -> None:
    pass


def configure_extensions(app: Flask) -> None:
    pass


def configure_views(app: Flask, app_folder_name: str = 'app', views_folder_name: str = 'views') -> None:
    views_directory = path.join(APP_FOLDER_PATH, 'views')
    module_files = [
        f for f in listdir(views_directory)
        if (f.endswith('.py')) and (not f.startswith('__'))
    ]

    for module_file in module_files:
        module_name = path.splitext(module_file)[0]
        module = import_module(f'{app_folder_name}.{views_folder_name}.{module_name}')

        for name in dir(module):
            item = getattr(module, name)
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
                break


def create_app() -> Flask:
    app = Flask(__name__)

    configure_views(app)

    return app
