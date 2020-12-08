from flask.wrappers import Response
from flask.templating import render_template
from flask.globals import request

from admin.api import Blueprint
from geomex import service

home = Blueprint('home', __name__)


@home.route('/', methods=['GET', 'POST'])
def index() -> Response:
    context = {}
    if request.method == 'POST':
        postal_code = request.form.get('zipcode').strip()
        neighborhoods = service.get_by_postal_code(postal_code)
        context['neighborhoods'] = neighborhoods
    return Response(render_template('zipcode.html', **context))
