from datetime import datetime
from flask import Blueprint, jsonify, render_template
from typing import Dict
from werkzeug import Response

from app.lib.utils import m_include, m_layout, m_macro, normalize_template_name


class Module(Blueprint):
    '''
    Custom Flask Blueprint extension with additional methods for convenience.

    :param name: The name of the blueprint.
    :type name: str

    :param import_name: The name of the current module.
    :type import_name: str

    :param static_folder: The folder with static files. Defaults to 'static'.
    :type static_folder: str, optional

    :param static_url_path: The URL prefix for static files. Defaults to None.
    :type static_url_path: str, optional

    :param template_folder: The folder with templates. Defaults to 'templates'.
    :type template_folder: str, optional

    :param url_prefix: The URL prefix for the blueprint. Defaults to None.
    :type url_prefix: str, optional

    :param kwargs: Additional keyword arguments accepted by Flask's Blueprint constructor.
    '''

    def __init__(self, name: str, import_name: str, static_folder: str = 'static', static_url_path: str = None, template_folder: str = 'templates', url_prefix: str = None, **kwargs) -> None:
        '''
        Initialize the Module instance.

        :param name: The name of the blueprint.
        :type name: 
        
        :param import_name: The name of the current module.
        :type import_name: str

        :param static_folder: The folder with static files. Defaults to 'static'.
        :type static_folder: str, optional

        :param static_url_path: The URL prefix for static files. Defaults to None.
        :type static_url_path: str, optional

        :param template_folder: The folder with templates. Defaults to 'templates'.
        :type template_folder: str, optional

        :param url_prefix: The URL prefix for the blueprint. Defaults to None.
        :type url_prefix: str, optional
        
        :param kwargs: Additional keyword arguments accepted by Flask's Blueprint constructor.
        '''
        Blueprint.__init__(self, name, import_name, static_folder, static_url_path, template_folder, url_prefix, **kwargs)

    def jsonify(self, *args, **kwargs) -> Response:
        '''
        A wrapper around Flask's jsonify function.

        :param args: Variable positional arguments to be passed to jsonify.
        :param kwargs: Variable keyword arguments to be passed to jsonify.

        :return: The JSON response.
        :rtype: Response
        '''
        return jsonify(*args, **kwargs)

    def render_template(self, template_name: str, data: Dict[object, object] = {}) -> str:
        '''
        Renders a template with additional data, including the current timestamp.

        :param template_name: The name of the template file.
        :type template_name: str
        
        :param data: Additional data to be passed to the template.
        :type data: Dict[object, object]

        :return: The rendered template content.
        :rtype: str
        '''
        context = {
            'm_inc': lambda include_name: m_include(self.name, include_name),
            'm_layout': lambda layout_name: m_layout(self.name, layout_name),
            'm_macro': lambda macro_name: m_macro(self.name, macro_name),
            'dt_now': datetime.now(),
            **data
        }
        return render_template(f'{self.name}/{normalize_template_name(template_name)}', **context)
