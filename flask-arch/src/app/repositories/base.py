from flask_sqlalchemy.model import Model
from sqlalchemy import (
    ColumnElement, UnaryExpression,
    and_
)
from sqlalchemy.orm import Query
from typing import List
from app.extensions import database


class BaseRepository():
    def add_entity(self, model: Model) -> None:
        try:
            database.session.add(model)
            database.session.commit()
        except Exception as e:
            database.session.rollback()
            raise e

    def delete_entity(self, model: Model) -> None:
        try:
            database.session.delete(model)
            database.session.commit()
        except Exception as e:
            database.session.rollback()
            raise e

    def _find_by(self, model_cls: Model, filters: List[ColumnElement[bool]]) -> Model:
        model: Model = model_cls.query.filter(
            and_(*filters)
        ).first()

        return model

    def _find_all_by(
        self,
        model_cls: Model,
        filter_clauses: List[ColumnElement[bool]] = None,
        order_clauses: List[UnaryExpression] = None
    ) -> List[Model]:

        query: Query = model_cls.query

        if filter_clauses:
            query = query.filter(and_(*filter_clauses))

        if order_clauses:
            query = query.order_by(*order_clauses)

        models: List[Model] = query.all()

        return models
