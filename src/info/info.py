from flask import Blueprint
from . import views

blueprint = Blueprint("info", __name__, template_folder="templates")
# Info page
blueprint.add_url_rule('/info', 'info', views.info)
