from datetime import datetime
from flask import Blueprint, render_template as f_render_template
from typing import Dict


_TEMPLATE_EXTENSION = '.jinja'
_LAYOUTS_FOLDER = 'layouts'
_INCLUDES_FOLDER = 'includes'
_MACROS_FOLDER = 'macros'


def _normalize_template_name(template_name: str) -> str:
    '''
    Ensure that a template name has the correct extension.

    :param template_name: The name of the template.
    :type template_name: str

    :return: The normalized template name.
    :rtype: str
    '''
    if not template_name.endswith(_TEMPLATE_EXTENSION):
        template_name += _TEMPLATE_EXTENSION

    return template_name


def layout(layout_name: str) -> str:
    '''
    Format the name of a layout template.

    :param layout_name: The name of the layout template.
    :type layout_name: str

    :return: The formatted layout template name.
    :rtype: str
    '''
    return f'{_LAYOUTS_FOLDER}/{_normalize_template_name(layout_name)}'


def include(include_name: str) -> str:
    '''
    Format the name of an include template.

    :param include_name: The name of the include template.
    :type include_name: str

    :return: The formatted include template name.
    :rtype: str
    '''
    return f'{_INCLUDES_FOLDER}/{_normalize_template_name(include_name)}'


def macro(macro_name: str) -> str:
    '''
    Format the name of a macro template.

    :param macro_name: The name of the macro template.
    :type macro_name: str

    :return: The formatted macro template name.
    :rtype: str
    '''
    return f'{_MACROS_FOLDER}/{_normalize_template_name(macro_name)}'


def render_template(blueprint: Blueprint, template_name: str, data: Dict[object, object] = {}) -> str:
    '''
    Renders a template with additional data, including the current timestamp.

    :param blueprint: The blueprint to which the template belongs.
    :type blueprint: Blueprint

    :param template_name: The name of the template file.
    :type template_name: str

    :param data: Additional data to be passed to the template.
    :type data: Dict[object, object]

    :return: The rendered template content.
    :rtype: str
    '''
    context = {
        '_inc': lambda include_name: f'{blueprint.name}/{include(include_name)}',
        '_layout': lambda layout_name: f'{blueprint.name}/{layout(layout_name)}',
        '_macro': lambda macro_name: f'{blueprint.name}/{macro(macro_name)}',
        'dt_now': datetime.now(),
        **data
    }
    return f_render_template(f'{blueprint.name}/{_normalize_template_name(template_name)}', **context)
