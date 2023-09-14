from flask import render_template
from typing import Dict


__TEMPLATE_EXTENSION: str = '.html.j2'
__PAGE_PATH: str = 'pages/{name}/'
__COMPONENT_PATH: str = 'components/{component_name}'
__LAYOUT_PATH: str = 'layouts/{layout_name}'


def complete_template_name(template_name: str) -> str:
    if not template_name.endswith(__TEMPLATE_EXTENSION):
        template_name += __TEMPLATE_EXTENSION

    return template_name


def component(*component_data):
    component_name: str = ''
    component_path: str = ''

    if len(component_data) == 1:
        component_name = component_data[0]
    elif len(component_data) == 2:
        component_name = component_data[1]
        module_name: str = component_data[0]
        component_path = __PAGE_PATH.format(
            name=module_name
        )

    component_path += __COMPONENT_PATH.format(
        component_name=complete_template_name(component_name)
    )

    return component_path


def layout(layout_name: str) -> str:
    return __LAYOUT_PATH.format(
        layout_name=complete_template_name(layout_name)
    )


def render_page(page_name: str, data: Dict[str, object] = None) -> str:
    page_path: str = __PAGE_PATH.format(
        name=complete_template_name(page_name)
    )

    return render_template(page_path, data=data)
