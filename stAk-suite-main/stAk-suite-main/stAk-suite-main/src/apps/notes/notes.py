from flask import Blueprint
from . import views

blueprint = Blueprint("notes", __name__, template_folder="templates")

blueprint.add_url_rule('/notes', 'notes', views.notes)