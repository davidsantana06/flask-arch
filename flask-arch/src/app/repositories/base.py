from flask_sqlalchemy.model import Model
from sqlalchemy import (
    ColumnElement,
    and_
)
from typing import List
from app.extensions import database


class Repository():
    def add_entity(self, model: Model) -> None:
        database.session.add(model)
        database.session.commit()

    def delete_entity(self, model: Model) -> None:
        database.session.delete(model)
        database.session.commit()

    def _find_by(self, model_cls: Model, filters: List[ColumnElement[bool]]) -> Model:
        model: Model = model_cls.query.filter(
            and_(*filters)
        ).first()

        return model

    def _find_all_by(self, model_cls: Model, filters: List[ColumnElement[bool]]) -> List[Model]:
        models: List[Model] = model_cls.query.filter(
            and_(*filters)
        ).all()

        return models
