from flask_restful import Resource
from webargs.flaskparser import use_kwargs
from geomex import service
from geomex.schemas import GeomexSchema, ZipcodeArgs


class Geomex(Resource):
    @use_kwargs(ZipcodeArgs, location='querystring')
    def get(self, zipcode):
        neighborhoods = service.get_by_postal_code(zipcode)
        if not neighborhoods:
            raise

        neighborhood = neighborhoods[0]
        return GeomexSchema().dump({
            "zipcode": neighborhood.postal_code,
            "state": neighborhood.municipality.state,
            "municipality": neighborhood.municipality,
            "neighborhoods": neighborhoods
        })
