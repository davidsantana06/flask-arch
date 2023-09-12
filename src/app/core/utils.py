from flask import render_template
from typing import Dict


def render_page(page_name: str, data: Dict[str, object] = None) -> str:
    if not page_name.endswith('.html.j2'):
        page_name += '.html.j2'

    return render_template(f'pages/{page_name}', data=data)
