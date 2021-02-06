from flask.wrappers import Response
from flask.templating import render_template
from admin.api import Blueprint

home = Blueprint('home', __name__)

@home.route('/')
def index() -> Response:
    return Response(render_template('welcome.html'))
