from flask import render_template as flask_render_template
from typing import Dict


TEMPLATE_EXTENSION = '.html.j2'


def complete_template_name(template_name: str) -> str:
    if not template_name.endswith(TEMPLATE_EXTENSION):
        template_name += TEMPLATE_EXTENSION

    return template_name


def render_template(template_name: str, data: Dict[str, object] = {}) -> str:
    return flask_render_template(complete_template_name(template_name), **data)


def template(template_name: str) -> str:
    return complete_template_name(template_name)
