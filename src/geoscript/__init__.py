import os
# noinspection PyPackageRequirements
from pandas import read_csv

from geomex.models import Neighborhood, Municipality, State


# noinspection PyUnresolvedReferences
class Geomex:
    def __init__(self):
        path_doc = os.path.join(
            os.path.abspath('..'),
            "src",
            "geoscript",
            "sepomex.csv"
        )
        self.doc = read_csv(
            path_doc,
            engine="python",
            sep="\|",
            header=1,
            dtype={'d_codigo': str},
            usecols=["d_codigo", "d_asenta", "D_mnpio", "d_estado"],
            encoding="ISO-8859-1"
        )

    def run(self):
        for i, row in self.doc.iterrows():
            postal_code = row.get("d_codigo").strip()
            neighborhood_name = row.get("d_asenta").strip()
            state_name = row.get("d_estado").strip()
            municipality_name = row.get("D_mnpio").strip()

            state = State.query.filter_by(name=state_name).scalar()
            if not state:
                state = State()
                state.name = state_name

            municipality = Municipality.query.filter_by(
                name=municipality_name,
                state_id=state.id
            ).first()
            if not municipality:
                municipality = Municipality()
                municipality.name = municipality_name
                municipality.state = state

            neighborhood = Neighborhood.query.filter_by(
                postal_code=postal_code,
                name=neighborhood_name,
                municipality_id=municipality.id
            ).first()
            if not neighborhood:
                neighborhood = Neighborhood()
                neighborhood.name = neighborhood_name
                neighborhood.postal_code = postal_code
                neighborhood.municipality = municipality

            neighborhood.save()
            print(neighborhood)

