from flask import Blueprint
from . import views

blueprint = Blueprint("rsa", __name__, template_folder="templates", url_prefix="/tools")

blueprint.add_url_rule('/rsa', 'rsa', views.rsa, methods = ["GET", "POST"])
