from flask.wrappers import Response
from flask.templating import render_template
from flask.globals import request
from flask.helpers import url_for
from werkzeug.utils import redirect
from commons.api import Blueprint
from user import service

user = Blueprint('user', __name__)

@user.route('/register', methods=['GET', 'POST'])
def index() -> Response:
    context = {}
    return Response(render_template('register.html', **context))


@user.route('/login', methods=['GET', 'POST'])
def login() -> Response:
    context = {}

    if request.method == 'POST':
        user_auth = service.login(request.form)
        if user_auth:
            access_token = service.access_token(user_auth)
            return redirect(url_for('home.index'))

    return Response(render_template('login.html', **context))
