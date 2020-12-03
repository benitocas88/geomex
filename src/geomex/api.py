from flask_restful import Resource
from webargs.flaskparser import use_kwargs

from geomex import service
from geomex.schemas import PostCodeArgs, GeomexSchema


class Geomex(Resource):
    @use_kwargs(PostCodeArgs, location='querystring')
    def get(self, postcode: str):
        neighborhoods = service.get_by_postal_code(postcode)

        if not neighborhoods:
            raise

        neighborhood = neighborhoods[0]
        data = {
            "postal_code": neighborhood.postal_code,
            "state": neighborhood.municipality.state,
            "municipality": neighborhood.municipality,
            "neighborhoods": neighborhoods
        }

        return GeomexSchema().dump(data)
