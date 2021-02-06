from typing import List
from geomex.models import Neighborhood


# noinspection PyUnresolvedReferences
class GeomexService:
    @staticmethod
    def get_by_postal_code(zipcode) -> List[Neighborhood]:
        return Neighborhood.query.filter_by(
            postal_code=zipcode
        ).order_by(Neighborhood.name).all()
