from flask import Response
from flask.templating import render_template
from flask.views import View
from geomex.service import GeomexService

from commons.api import Blueprint
from geomex.schemas import ZipcodeArgs
from webargs.flaskparser import use_kwargs
geomex = Blueprint("geomex", __name__, url_prefix="/dashboard")


@geomex.route("/sepomex", methods=("GET", "POST"))
@use_kwargs(ZipcodeArgs, location="querystring")
def index(**kwargs):
    zipcode = kwargs.get("zipcode")

    context = {}
    if zipcode:
        geo = GeomexService()
        context["neighborhoods"] = geo.get_by_postal_code(zipcode)
    return Response(render_template("geomex.html", **context))
