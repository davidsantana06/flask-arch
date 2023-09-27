from flask import redirect as redirect, render_template, url_for
from typing import Dict, Tuple, Union


TEMPLATE_EXTENSION = '.html.j2'
PAGE_PATH = 'pages/{name}/'
COMPONENT_PATH = 'components/{component_name}'
LAYOUT_PATH = 'layouts/{layout_name}'


def complete_template_name(template_name: str) -> str:
    if not template_name.endswith(TEMPLATE_EXTENSION):
        template_name += TEMPLATE_EXTENSION

    return template_name


def component(*component_data: Union[str, Tuple[str, str]]) -> str:
    component_name = ''
    component_path = ''

    if len(component_data) == 1:
        component_name = component_data[0]
    elif len(component_data) == 2:
        component_name = component_data[1]
        module_name = component_data[0]
        component_path = PAGE_PATH.format(
            name=module_name
        )

    component_path += COMPONENT_PATH.format(
        component_name=complete_template_name(component_name)
    )

    return component_path


def layout(layout_name: str) -> str:
    return LAYOUT_PATH.format(
        layout_name=complete_template_name(layout_name)
    )


def redirect_to(endpoint: str) -> str:
    return redirect(url_for(endpoint))


def render_page(page_name: str, data: Dict[str, object] = {}) -> str:
    page_path = PAGE_PATH.format(
        name=complete_template_name(page_name)
    )

    return render_template(page_path, **data)
