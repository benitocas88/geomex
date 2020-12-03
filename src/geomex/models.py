from admin.models import Model, db


class State(Model, db.Model):
    __tablename__ = 'state'

    name = db.Column(db.String(length=90), nullable=False)


class Municipality(Model, db.Model):
    __tablename__ = 'municipality'

    name = db.Column(db.String(length=90), nullable=False)
    state_id = db.Column(
        db.Integer,
        db.ForeignKey('state.id', name='fk_state__municipality')
    )
    state = db.relationship(
        State,
        uselist=False,
        lazy='select'
    )


class Neighborhood(Model, db.Model):
    __tablename__ = 'neighborhood'

    name = db.Column(db.String(length=90), nullable=False)
    postal_code = db.Column(db.String(length=5), nullable=False, index=True)
    municipality_id = db.Column(
        db.Integer,
        db.ForeignKey('municipality.id', name='fk_municipality__neighborhood')
    )
    municipality = db.relationship(Municipality, uselist=False, lazy='select')
