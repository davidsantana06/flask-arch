from flask import Flask
from app.lib.utils import component, format_dt, layout, today_date


def configure_jinja_env(app: Flask) -> None:
    app.jinja_env.globals.update({
        'component': component,
        'layout': layout,
        'today_date': today_date,
        'format_dt': format_dt
    })
