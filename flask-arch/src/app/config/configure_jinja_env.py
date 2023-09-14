from flask import Flask
from app.utils.jinja import component, layout


def configure_jinja_env(app: Flask) -> None:
    app.jinja_env.globals.update({
        'component': component,
        'layout': layout
    })