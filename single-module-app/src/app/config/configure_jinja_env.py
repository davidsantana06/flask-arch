from flask import Flask
from app.lib.utils import component, format_datetime, layout


def configure_jinja_env(app: Flask) -> None:
    app.jinja_env.globals.update({
        'component': component,
        'layout': layout,
        'format_datetime': format_datetime
    })
