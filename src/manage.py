from os import getenv
from flask.templating import render_template
from flask.wrappers import Response

from app import create_app
from geomex.models import State, Municipality
from geoscript import Geomex

env = getenv('FLASK_ENV')
app = create_app(env)


@app.route('/')
def home_state() -> Response:
    states = State.query.all()
    return render_template('geomex/state.html', states=states)


@app.route('/state/<int:state_id>')
def home_municipality(state_id: int) -> Response:
    state = State.query.get(state_id)
    return render_template('geomex/municipality.html', state=state)


@app.route('/municipality/<int:municipality_id>')
def home_neighborhood(municipality_id: int) -> Response:
    municipality = Municipality.query.get(municipality_id)
    return render_template(
        'geomex/neighborhood.html',
        municipality=municipality
    )


@app.cli.command('geo')
def geoscript():
    geomex = Geomex()
    geomex.run()
