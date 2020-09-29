from os import getenv
from flask.templating import render_template
from flask.wrappers import Response

from app import create_app
from geoscript import Geomex

env = getenv('FLASK_ENV', 'development')
app = create_app(env)


@app.route('/')
def home_state() -> Response:
    return render_template('geomex/zipcode.html')


@app.cli.command('geo')
def geoscript():
    geomex = Geomex()
    geomex.run()
