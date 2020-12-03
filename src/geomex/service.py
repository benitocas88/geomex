from typing import List

from geomex.models import Neighborhood


# noinspection PyUnresolvedReferences
class GeomexService:
    @staticmethod
    def get_by_postal_code(postcode: str) -> List[Neighborhood]:
        return Neighborhood.query.filter_by(
            postal_code=postcode
        ).order_by(Neighborhood.name).all()
