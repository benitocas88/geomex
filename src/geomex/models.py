from sqlalchemy.orm.attributes import Mapped
from commons.models import Model, db


class State(Model):
    __tablename__ = 'states'

    name: Mapped[str] = db.mapped_column(db.String(length=90), nullable=False)


class Municipality(Model):
    __tablename__ = 'municipalities'

    name: Mapped[str] = db.mapped_column(db.String(length=90), nullable=False)
    state_id: Mapped[int] = db.Column(db.ForeignKey('states.id', name='fk_states__municipalities'))
    state: Mapped[State] = db.relationship(State, uselist=False, lazy='select')


class Neighborhood(Model):
    __tablename__ = 'neighborhoods'

    name: Mapped[str] = db.mapped_column(db.String(length=90), nullable=False)
    postal_code: Mapped[str] = db.mapped_column(db.String(length=5), nullable=False, index=True)
    # settlement = db.Column(db.String(length=30))
    municipality_id: Mapped[int] = db.mapped_column(db.ForeignKey('municipalities.id', name='fk_municipalities__neighborhoods'))
    municipality: Mapped[Municipality] = db.relationship(Municipality, uselist=False, lazy='select')
