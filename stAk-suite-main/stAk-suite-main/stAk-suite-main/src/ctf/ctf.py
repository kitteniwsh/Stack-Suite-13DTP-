from flask import Blueprint
from . import views

blueprint = Blueprint("ctf", __name__, template_folder="templates")

blueprint.add_url_rule('/ctf', 'ctf', views.ctf)