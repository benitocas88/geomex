from flask.blueprints import Blueprint
from flask_restful import Api

from geomex.api import Geomex

api_v1 = Blueprint('api', __name__, url_prefix='/v1.0')
api = Api(api_v1)

api.add_resource(Geomex, "/postalCodes")
