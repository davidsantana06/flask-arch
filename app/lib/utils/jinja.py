TEMPLATE_EXTENSION = '.jinja'
LAYOUTS_FOLDER = 'layouts'
INCLUDES_FOLDER = 'includes'
MACROS_FOLDER = 'macros'


def normalize_template_name(template_name: str) -> str:
    '''
    Ensure that a template name has the correct extension.

    :param template_name: The name of the template.
    :type template_name: str

    :return: The normalized template name.
    :rtype: str
    '''
    if not template_name.endswith(TEMPLATE_EXTENSION):
        template_name += TEMPLATE_EXTENSION

    return template_name


def layout(layout_name: str) -> str:
    '''
    Format the name of a layout template.

    :param layout_name: The name of the layout template.
    :type layout_name: str

    :return: The formatted layout template name.
    :rtype: str
    '''
    return f'{LAYOUTS_FOLDER}/{normalize_template_name(layout_name)}'


def m_layout(module_name: str, layout_name: str) -> str:
    '''
    Format the name of a layout template within a specific module.

    :param module_name: The name of the module.
    :type module_name: str

    :param layout_name: The name of the layout template.
    :type layout_name: str

    :return: The formatted layout template name within the specified module.
    :rtype: str
    '''
    return f'{module_name}/{layout(layout_name)}'


def include(include_name: str) -> str:
    '''
    Format the name of an include template.

    :param include_name: The name of the include template.
    :type include_name: str

    :return: The formatted include template name.
    :rtype: str
    '''
    return f'{INCLUDES_FOLDER}/{normalize_template_name(include_name)}'


def m_include(module_name: str, include_name: str) -> str:
    '''
    Format the name of an include template within a specific module.

    :param module_name: The name of the module.
    :type module_name: str

    :param include_name: The name of the include template.
    :type include_name: str

    :return: The formatted include template name within the specified module.
    :rtype: str
    '''
    return f'{module_name}/{include(include_name)}'


def macro(macro_name: str) -> str:
    '''
    Format the name of a macro template.

    :param macro_name: The name of the macro template.
    :type macro_name: str

    :return: The formatted macro template name.
    :rtype: str
    '''
    return f'{MACROS_FOLDER}/{normalize_template_name(macro_name)}'


def m_macro(module_name: str, macro_name: str) -> str:
    '''
    Format the name of a macro template within a specific module.

    :param module_name: The name of the module.
    :type module_name: str

    :param macro_name: The name of the macro template.
    :type macro_name: str

    :return: The formatted macro template name within the specified module.
    :rtype: str
    '''
    return f'{module_name}/{macro(macro_name)}'
