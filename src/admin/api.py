from flask.blueprints import Blueprint as Base
from flask_restful import Api

from geomex.api import Geomex


class Blueprint(Base):
    def __init__(self, *args, **kwargs):
        super(Blueprint, self).__init__(
            *args,
            **kwargs,
            template_folder='templates'
        )


api_v1 = Blueprint('api', __name__, url_prefix='/v1.0')
api = Api(api_v1)

api.add_resource(Geomex, '/zipcodes')
