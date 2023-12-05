from flask import Flask
from app.lib.utils import format_dt, include, layout, macro


def configure_jinja_env(app: Flask) -> None:
    app.jinja_env.globals.update({
        'inc': include,
        'layout': layout,
        'macro': macro,
        'format_dt': format_dt
    })
