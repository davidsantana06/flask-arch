from flask import Flask

from app.lib.core import include, layout, macro
from app.lib.utils import format_dt


def configure_jinja_env(app: Flask) -> None:
    app.jinja_env.globals.update({
        'inc': include,
        'layout': layout,
        'macro': macro,
        'format_dt': format_dt
    })
