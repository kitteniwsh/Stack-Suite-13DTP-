from flask import Blueprint
from . import views

blueprint = Blueprint("about", __name__, template_folder="templates")

blueprint.add_url_rule('/about', 'about', views.about)
