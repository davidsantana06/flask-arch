from flask import Flask
from app.lib.utils import component, dt_now, format_dt, layout


def configure_jinja_env(app: Flask) -> None:
    app.jinja_env.globals.update({
        'component': component,
        'layout': layout,
        'dt_now': dt_now,
        'format_dt': format_dt
    })
