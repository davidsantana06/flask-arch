from datetime import datetime
from flask import (
    Blueprint,
    render_template as f_render_template, url_for
)
from typing import Dict


_TEMPLATE_EXTENSION = '.jinja'
_LAYOUTS_FOLDER = 'layouts'
_INCLUDES_FOLDER = 'includes'
_MACROS_FOLDER = 'macros'
_CSS_EXTENSION = '.css'
_CSS_FILE = 'css/{}'
_JS_EXTENSION = '.js'
_JS_FILE = 'js/{}'
_IMG_FILE = 'img/{}'


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


def _generate_url_for_static(file_name: str, module: str = '') -> str:
    '''
    Retrieve the URL for a static file.

    :param file_name: The name of the static file.
    :type file_name: str

    :param module: The name of the module in which the static file is located.
    :type module: str

    :return: The URL for the static file.
    :rtype: str
    '''
    return url_for(f'{module}static', filename=file_name)


def css(css_name: str, module: str = '') -> str:
    '''
    Format the name of a CSS file.

    :param css_name: The name of the CSS file.
    :type css_name: str

    :param same_module: Whether the CSS file is in the same module as the template.
    :type same_module: bool

    :return: The formatted CSS file name.
    :rtype: str
    '''
    if not css_name.endswith(_CSS_EXTENSION):
        css_name += _CSS_EXTENSION
    return _generate_url_for_static(_CSS_FILE.format(css_name), module)


def img(img_name: str, module: str = '') -> str:
    '''
    Format the name of an image file.

    :param img_name: The name of the image file.
    :type img_name: str

    :param same_module: Whether the image file is in the same module as the template.
    :type same_module: bool

    :return: The formatted image file name.
    :rtype: str
    '''
    return _generate_url_for_static(_IMG_FILE.format(img_name), module)


def js(js_name: str, module: str = '') -> str:
    '''
    Format the name of a JS file.

    :param js_name: The name of the JS file.
    :type js_name: str

    :param same_module: Whether the JS file is in the same module as the template.
    :type same_module: bool

    :return: The formatted JS file name.
    :rtype: str
    '''
    if not js_name.endswith(_JS_EXTENSION):
        js_name += _JS_EXTENSION
    return _generate_url_for_static(_JS_FILE.format(js_name), module)


def render_template(blueprint: Blueprint, template_name: str, data: Dict[str, object] = {}) -> str:
    '''
    Renders a template with additional data, including the current datetime.

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
        '_css': lambda css_name: css(css_name, '.'),
        '_img': lambda img_name: img(img_name, '.'),
        '_js': lambda js_name: js(js_name, '.'),
        'current_datetime': datetime.now(),
        **data
    }
    return f_render_template(f'{blueprint.name}/{_normalize_template_name(template_name)}', **context)
