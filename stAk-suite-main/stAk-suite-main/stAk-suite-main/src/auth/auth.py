from flask import Blueprint
from . import views

blueprint = Blueprint("auth", __name__, template_folder="templates")

blueprint.add_url_rule('/authenticate/<page>', 'authenticate', views.authenticate, methods=["GET", "POST"])
blueprint.add_url_rule('/endsession', 'endsession', views.endsession)
