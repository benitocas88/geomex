from commons.models import Model, db


class State(Model):
    __tablename__ = 'states'

    name = db.Column(db.String(length=90), nullable=False)


class Municipality(Model):
    __tablename__ = 'municipalities'

    name = db.Column(db.String(length=90), nullable=False)
    state_id = db.Column(
        db.Integer,
        db.ForeignKey('states.id', name='fk_states__municipalities')
    )
    state = db.relationship(
        State,
        uselist=False,
        lazy='select'
    )


class Neighborhood(Model):
    __tablename__ = 'neighborhoods'

    name = db.Column(db.String(length=90), nullable=False)
    postal_code = db.Column(db.String(length=5), nullable=False, index=True)
    # settlement = db.Column(db.String(length=30))
    municipality_id = db.Column(
        db.Integer,
        db.ForeignKey('municipalities.id', name='fk_municipalities__neighborhoods')
    )
    municipality = db.relationship(Municipality, uselist=False, lazy='select')
