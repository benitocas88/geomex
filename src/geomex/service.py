from typing import List
from geomex.models import Neighborhood


class GeomexService:
    @staticmethod
    def get_by_postal_code(zipcode) -> List[Neighborhood]:
        return Neighborhood.query.filter_by(
            zipcode=zipcode
        ).order_by(Neighborhood.name).all()
