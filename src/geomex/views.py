from flask import Response
from flask.templating import render_template
from geomex.forms import ZipcodeForm
from geomex.service import GeomexService

from commons.api import Blueprint
from geomex.schemas import ZipcodeArgs
from webargs.flaskparser import use_kwargs
geomex = Blueprint("geomex", __name__, url_prefix="/dashboard")


@geomex.route("/sepomex/", methods=("GET",))
@use_kwargs(ZipcodeArgs, location="querystring")
def index(**kwargs):
    form = ZipcodeForm(data=kwargs)

    if form.zipcode.data:
        geo = GeomexService()
        form.neighborhoods.choices = [
            (s.id, s.name)
            for s in geo.get_by_postal_code(form.zipcode.data)
        ]
    return Response(render_template("geomex.html", form=form))
