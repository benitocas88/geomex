import csv
import os.path
import pathlib


class Sepomex:
    def read_file(self):
        route = os.path.abspath(os.path.join("geomex", "commands", "sepomex.txt"))
        file = pathlib.Path(route)

        if not (file.exists() and file.is_file()):
            raise FileNotFoundError()

        if file.suffix != ".txt":
            raise ValueError("invalid format file")

        csv_file = open(mode="r", file=file, encoding="utf8")
        csv_reader = csv.reader(csv_file, delimiter=",", dialect=csv.excel)
        headers = next(csv_reader)
        print(headers)

    def geo(self):
        self.read_file()
