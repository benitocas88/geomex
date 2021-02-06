from flask.blueprints import Blueprint as BlueprintBase
from flask_restful import Api

from geomex.api import Geomex


class Blueprint(BlueprintBase):
    def __init__(self, *args, **kwargs):
        super(Blueprint, self).__init__(
            *args,
            **kwargs,
            template_folder='templates'
        )

api_v1 = Blueprint('api_v1', __name__, url_prefix='/v1.0')
api = Api(api_v1)

api.add_resource(Geomex, '/zipcodes')
