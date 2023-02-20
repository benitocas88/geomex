from flask import Response
from flask.templating import render_template
from geomex.forms import ZipcodeForm
from geomex import service as geo

from commons.api import Blueprint
from geomex.schemas import ZipcodeArgs
from webargs.flaskparser import use_kwargs

geomex = Blueprint("geomex", __name__, url_prefix="/dashboard")


@geomex.route("/sepomex/", methods=("GET",))
@use_kwargs(ZipcodeArgs, location="querystring")
def index(**kwargs):
    form = ZipcodeForm(data=kwargs)

    if form.zipcode.data:
        form.neighborhoods.choices = [
            (g.id, f"{g.name} - ({g.settlement})")
            for g in geo.get_by_postal_code(form.zipcode.data)
        ]
    return Response(render_template("geomex.html", form=form))
