from flask import Blueprint
from . import views

blueprint = Blueprint("ctf", __name__, template_folder="templates")
# Main crypto page
blueprint.add_url_rule('/ctf', 'ctf', views.ctf)
