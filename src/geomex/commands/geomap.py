import csv
import os.path
import pathlib


class Sepomex:
    def read_file(self):
        route = os.path.abspath(os.path.join("geomex", "commands", "sepomex.xls"))
        file = pathlib.Path(route)

        if not (file.exists() and file.is_file()):
            raise FileNotFoundError()

        if file.suffix != ".xls":
            raise ValueError("invalid format file")

        from pandas import read_excel, DataFrame

        xls = read_excel(file, sheet_name=["Durango"])
        data = DataFrame(
            xls,
            columns=[
                "d_asenta",
            ],
        )

        print(data)

    def geo(self):
        self.read_file()
