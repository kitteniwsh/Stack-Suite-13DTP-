from flask import Blueprint
from . import views

blueprint = Blueprint("info", __name__, template_folder="templates")

blueprint.add_url_rule('/info', 'info', views.info)
