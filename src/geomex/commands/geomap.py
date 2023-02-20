import csv
import os.path
import pathlib
from geomex.models import Neighborhood, Municipality, State

COLUMNS = [
    "d_asenta",
    "d_tipo_asenta",
    "D_mnpio",
    "d_estado",
    "d_codigo",
]


class Sepomex:
    @staticmethod
    def read_file():
        route = os.path.abspath(os.path.join("geomex", "commands", "sepomex.xls"))
        file = pathlib.Path(route)

        if not (file.exists() and file.is_file()):
            raise FileNotFoundError()

        if file.suffix != ".xls":
            raise ValueError("invalid format file")

        from pandas.io.excel import ExcelFile, read_excel

        xls = ExcelFile(file)
        sheets = [sheet for sheet in xls.sheet_names if sheet.lower() != "nota"]

        for sheet in sheets:
            print(f"sheet migration started: {sheet}")
            reader = read_excel(file, sheet_name=sheet, dtype={"d_codigo": str}, engine="xlrd", usecols=COLUMNS)
            for _, row in reader.iterrows():
                state_name = row["d_estado"].strip()
                state = State.query.filter_by(name=state_name).first()
                if not state:
                    state = State(name=state_name)
                    state.save()

                municipality_name = row["D_mnpio"].strip()
                municipality = Municipality.query.filter_by(name=municipality_name, state=state).first()
                if not municipality:
                    municipality = Municipality(name=municipality_name, state=state)
                    municipality.save()

                neighborhood_name = row["d_asenta"].strip()
                zipcode = row["d_codigo"].strip()
                settlement = row["d_tipo_asenta"].strip()

                neighborhood = Neighborhood.query.filter_by(
                    name=neighborhood_name,
                    zipcode=zipcode,
                    municipality=municipality,
                    settlement=settlement,
                ).first()

                if not neighborhood:
                    Neighborhood(
                        name=neighborhood_name,
                        zipcode=zipcode,
                        settlement=settlement,
                        municipality=municipality,
                    ).save()
            print("Done!\n")

    def geo(self):
        self.read_file()
