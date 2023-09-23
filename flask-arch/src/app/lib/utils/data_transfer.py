from flask_wtf import FlaskForm
from typing import Dict, List


def dict_to_form(data: Dict[str, object], form: FlaskForm):
    for field in form:
        name = field.name

        if name in data:
            value = data[name]
            field.data = value
            data.pop(name)


def obj_to_form(obj: object, form: FlaskForm, reserverd_attrs: List[str] = []):
    for field in form:
        name = field.name

        if (hasattr(obj, name)) and (name not in reserverd_attrs):
            field.data = getattr(obj, name)


def form_to_obj(form: FlaskForm, obj: object, reserverd_attrs: List[str] = []):
    for field in form:
        name = field.name

        if name not in reserverd_attrs:
            field.populate_obj(obj, name)
