from os import getenv

from app import create_app

env = getenv("FLASK_ENV")
app = create_app(env)
app.app_context().push()


@app.cli.command("geo")
def run_geo():
    from geoscript import Geomex
    geo = Geomex()
    geo.run()
