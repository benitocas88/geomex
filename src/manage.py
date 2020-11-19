from os import getenv
from flask.templating import render_template
from flask.wrappers import Response
from flask.globals import request

from app import create_app

from geomex import service

env = getenv('FLASK_ENV', 'development')
app = create_app(env)


@app.route('/', methods=['GET', 'POST'])
def home() -> Response:
    context = {}

    if request.method == 'POST':
        postal_code = request.form.get('zipcode').strip()
        neighborhoods = service.get_by_postal_code(postal_code)
        context['neighborhoods'] = neighborhoods

    return Response(render_template('geomex/zipcode.html', **context))


@app.route('/users', methods=['GET', 'POST'])
def users() -> Response:
    return Response(render_template("user/user.html"))
