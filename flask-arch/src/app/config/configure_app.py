from datetime import timedelta
from flask import Flask
from typing import Dict
from app.constants import RESOURCES_FOLDER_PATH


__STATIC_FOLDER: str = f'{RESOURCES_FOLDER_PATH}/static'
__TEMPLATE_FOLDER: str = f'{RESOURCES_FOLDER_PATH}/templates'
__CONFIG: Dict[str, object] = {
    'SECRET_KEY': '' + \
        '| ------------------------------- |\n' + \
        '|  Flask Definitive Architecture  |\n' + \
        '|    github.com/davidsantana06    |\n' + \
        '| ------------------------------- |',
    'SQLALCHEMY_DATABASE_URI': '{dbms}://{username}:{password}@{server}/{database}'.format(
        dbms='mysql+mysqlconnector',
        username='',
        password='',
        server='',
        database=''
    ),
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'PERMANENT_SESSION_LIFETIME': timedelta(days=1)
}


def configure_app(app: Flask) -> None:
    app.static_folder = __STATIC_FOLDER
    app.template_folder = __TEMPLATE_FOLDER
    
    for name, param in __CONFIG.items():
        app.config[name] = param
        