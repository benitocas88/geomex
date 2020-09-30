from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declared_attr

from app import db


# https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/mixins.html?highlight=tablename#mixin-and-custom-base-classes
# noinspection PyUnresolvedReferences
class Mixin:
    @classmethod
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=90), nullable=False)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except IntegrityError as error:
            db.session.rollback()
            raise error


class State(Mixin, db.Model):
    __tablename__ = 'state'


class Municipality(Mixin, db.Model):
    __tablename__ = 'municipality'

    state_id = db.Column(
        db.Integer,
        db.ForeignKey('state.id', name='fk_state__municipality')
    )
    state = db.relationship(
        State,
        uselist=False,
        lazy='select'
    )


class Neighborhood(Mixin, db.Model):
    __tablename__ = 'neighborhood'

    postal_code = db.Column(db.String(length=5), nullable=False, index=True)
    municipality_id = db.Column(
        db.Integer,
        db.ForeignKey('municipality.id', name='fk_municipality__neighborhood')
    )
    municipality = db.relationship(Municipality, uselist=False, lazy='select')
