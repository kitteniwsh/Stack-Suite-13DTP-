from flask import Blueprint
from . import views

blueprint = Blueprint("auth", __name__, template_folder="templates")

blueprint.add_url_rule('/authenticate', 'authenticate', views.authenticate, methods=["GET", "POST"])
blueprint.add_url_rule('/register', 'register', views.register,methods=["GET", "POST"])
