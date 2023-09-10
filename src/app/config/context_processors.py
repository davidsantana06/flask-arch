from flask import Flask


def complete_template_filename(template_filename: str) -> str:
    if (not template_filename.endswith(('.html', '.j2'))):
        template_filename += '.html.j2'

    return template_filename


def layout(layout_filename: str) -> str:
    layout_path: str = 'layouts/{}'.format(
        complete_template_filename(layout_filename)
    )

    return layout_path


def component(*args) -> str:
    component_filename: str = ''
    component_path: str = ''

    if (len(args) == 1):
        component_filename = args[0]
        component_path = 'common'
    elif (len(args) == 2):
        component_filename = args[1]
        component_path = 'pages/{}'.format(args[0])

    component_path += '/components/{}'.format(
        complete_template_filename(component_filename)
    )

    return component_path


def configure_context_processors(app: Flask) -> None:
    app.jinja_env.globals.update(layout=layout)
    app.jinja_env.globals.update(component=component)
